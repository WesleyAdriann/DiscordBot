import discord
import os
from logger import logg

logger = logg('main_bot')

bot = discord.Client()
if not discord.opus.is_loaded():
    discord.opus.load_opus('opus')


logger.info('Starts Bot, waiting to be ready')
@bot.event
async def on_ready():
    logger.info('Bot is ready')
    activity = discord.Activity(
        name=">ajuda",
        type=discord.ActivityType.listening,
        )
    await bot.change_presence(activity=activity,)

@bot.event
async def on_message(message):
    if message.content[0] != '>':
        return

    channel = message.channel

    logger.info(f"{message.author} | {message.content}")
        
    
    if message.content == '>ajuda':
        embed = discord.Embed(
            title="Comandos",
            description="Todos os comandos começam com '>'",
            color=discord.Color.magenta(),
        )
        embed.add_field(name=">youtube pesquisa", value="Busca video no youtube //em construção")
        embed.add_field(name=">info", value="Exibe informações do servidor")
        embed.add_field(name=">limpar numero", value="Exclui quantidade de menssagens pelo numero passado")
        embed.set_thumbnail(url="https://cdn.discordapp.com/app-icons/600866134924984320/fe5bacc16fefd66e5c4690c2b12e2d16.png")
        await channel.send(embed=embed)
        return

    if message.content == '>info':
        embed = discord.Embed(
            title="Comandos",
            description="Todos os comandos começam com '>'",
            color=discord.Color.magenta(),
        )
        embed.add_field(name=">youtube pesquisa", value="Busca video no youtube //em construção")
        embed.add_field(name=">info", value="Exibe informações do servidor")
        embed.add_field(name=">limpar numero", value="Exclui quantidade de menssagens pelo numero passado")
        embed.set_thumbnail(url="https://cdn.discordapp.com/app-icons/600866134924984320/fe5bacc16fefd66e5c4690c2b12e2d16.png")
        await channel.send(embed=embed)
        return

    if message.content == '>entrar':
        voiceChannel = message.author.voice
        # logger.info(message.author.voice)
        logger.info('aa')
        if voiceChannel == None:
            await channel.send("Você não esta em uma canal de voz.")
            return False

        logger.info('here')
        state = bot.get_voice_state(message.server)
        logger.info(state)
        logger.info(state.voice)
        if state.voice == None:
            state.voice = await bot.join_voice_channel(voiceChannel)
        else:
        await state.voice.move_to(voiceChannel)

        return

    # await channel.send('ok')

bot.run(os.environ['DISCORD_BOT_KEY'])