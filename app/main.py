import discord
from discord.ext import commands

import datetime
import logging
import os

from logger import logg

logger = logg()

# CONFIG LOGGER
# logger = logging.getLogger('main_bot')
# logger.setLevel(logging.DEBUG)
# ch = logging.StreamHandler()
# ch.setLevel(logging.DEBUG)
# formatter = logging.Formatter('%(message)s')
# ch.setFormatter(formatter)
# logger.addHandler(ch)


logger.info('Starts Bot')

bot = commands.Bot(command_prefix=">", description="This is a fucking bot")

@bot.event
async def on_ready():
    logger.info('Bot is ready')
    activity = discord.Activity(
        name=">ajuda",
        type=discord.ActivityType.listening,
        )
    await bot.change_presence(activity=activity,)


@bot.command()
async def ajuda(ctx):
    embed = discord.Embed(
        title="Comandos",
        description="Todos os comandos começam com '>'",
        color=discord.Color.magenta(),
        )
    embed.add_field(name=">youtube valor", value="Busca video no youtube //em construção")
    embed.add_field(name=">info", value="Exibe informações do servidor")
    embed.set_thumbnail(url="https://cdn.discordapp.com/app-icons/600866134924984320/fe5bacc16fefd66e5c4690c2b12e2d16.png")
    await ctx.send(embed=embed)

@bot.command()
async def info(ctx):
    logging.info('This is an info message')
    embed = discord.Embed(
        title=f"{ctx.guild.name}",
        # description="HUE",
        timestamp=datetime.datetime.utcnow(),
        color=discord.Color.magenta()
        )
    embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Server owner", value=f"{ctx.guild.owner}")
    embed.add_field(name="Server region", value=f"{ctx.guild.region}")
    embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
    # embed.set_thumbnail(url=f"{ctx.guild.banner}")
    await ctx.send(embed=embed)

@bot.command()
async def youtube(ctx, *, search):
    query_string = parse.urlencode({'search_query': search})
    html_content = request.urlopen('http://www.youtube.com/results?' + query_string)
    search_results = re.findall('href=\"\\/watch\\?v=(.{11})', html_content.read().decode())
    await ctx.send('https://www.youtube.com/watch?v=' + search_results[0])

@bot.command()
async def tests_(ctx):
    await ctx.send("ok")


bot.run(os.environ['DISCORD_BOT_KEY'])