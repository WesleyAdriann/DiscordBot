import discord
from discord.ext import commands
from logger import logg
import os
import asyncio

logger = logg('main_bot')
if not discord.opus.is_loaded():
    discord.opus.load_opus('opus')


class Music:
    def __init__(self, bot):
        self.bot = bot
        self.voice_states = {}

    def get_voice_state(self, server):
        state = self.voice_state.get(server.id)
        if state is None:
            state = VoiceState(self.bot)
            self.voice_states[server.id] = state
        return state
    
    async def create_voice_client(self, channel):
        voice = await self.bot.join_voice_channel(channel)
        state = self.get_voice_state(channel.server)
        state.voice = voice

    def __unload(self):
        for state in self.voice_states.values():
            try:
                state.audio_player.cancel()
                if state.voice:
                    self.bot.loop.create_task(state.voice.disconnect())
            except:
                pass

    @commands.command(pass_context = True, no_pm = True)
    async def entrar(self, ctx, *, channel):
        await self.bot.say('ok')



bot = commands.Bot(command_prefix = ">")
bot.add_cog(Music(bot))

logger.info('Starts Bot, waiting to be ready')

@bot.event
async def on_ready():
    logger.info(f"Bot {bot.user} is ready")
    activity = discord.Activity(
        name=">ajuda",
        type=discord.ActivityType.listening,
        )
    await bot.change_presence(activity=activity,)

bot.run(os.environ['DISCORD_BOT_KEY'])