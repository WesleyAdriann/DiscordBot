import discord
from discord.ext import commands
from discord.utils import get
import logging
import os
from urllib import parse, request
import re
from logger import logg
import asyncio


logger = logg('main_bot')

bot = commands.Bot(command_prefix = ">")
ops = discord.opus.load_opus('opus')
logger.info(ops)
logger.info('Starts Bot, waiting to be ready')


# EVENTOS
@bot.event
async def on_ready():
    logger.info('Bot is ready')
    activity = discord.Activity(
        name=">ajuda",
        type=discord.ActivityType.listening,
        )
    await bot.change_presence(activity=activity,)

@bot.event
async def on_command_error(ctx, err):
    logger.info(err)
    if isinstance(err, commands.CommandNotFound):
        await ctx.send("Comando invalido")

# COMANDOS
@bot.command()
async def ajuda(ctx):
    logger.info(f"{ctx.author} | {ctx.message.content}")
    embed = discord.Embed(
        title="Comandos",
        description="Todos os comandos começam com '>'",
        color=discord.Color.magenta(),
        )
    embed.add_field(name=">youtube pesquisa", value="Busca video no youtube //em construção")
    embed.add_field(name=">info", value="Exibe informações do servidor")
    embed.add_field(name=">limpar numero", value="Exclui quantidade de menssagens pelo numero passado")
    embed.set_thumbnail(url="https://cdn.discordapp.com/app-icons/600866134924984320/fe5bacc16fefd66e5c4690c2b12e2d16.png")
    await ctx.send(embed=embed)

@bot.command()
async def info(ctx):
    logger.info(f"{ctx.author} | {ctx.message.content}")
    embed = discord.Embed(
        title=f"{ctx.guild.name}",
        color=discord.Color.magenta()
        )
    embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Server owner", value=f"{ctx.guild.owner}")
    embed.add_field(name="Server region", value=f"{ctx.guild.region}")
    embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
    await ctx.send(embed=embed)

@bot.command()
async def youtube(ctx, *, search):
    logger.info(f"{ctx.author} | {ctx.message.content}")
    query_string = parse.urlencode({'search_query': search})
    html_content = request.urlopen('http://www.youtube.com/results?' + query_string)
    search_results = re.findall('href=\"\\/watch\\?v=(.{11})', html_content.read().decode())
    channel = ctx.author.voice
    await ctx.send('https://www.youtube.com/watch?v=' + search_results[0])

@bot.command()
async def limpar(ctx, amount : int):
    logger.info(f"{ctx.author} | {ctx.message.content}")
    await ctx.channel.purge(limit=amount)

@limpar.error
async def limpar_error(ctx, error):
    logger.info(f"{ctx.author} | {ctx.message.content}")
    if isinstance(err, commands.MissingRequiredArgument):
        await ctx.send('Informe a quantidade que deseja apagar.')

@bot.command(pass_context=True)
async def test(ctx):
    logger.info('start test')
    # voice = get(bot.voice_clients, guild=ctx.guild)
    # logger.info(f"{ctx.message.author.voice.channel.id}")
    # logger.info(f"{ctx.author}")
    # channel = ctx.message.author.voice.channel
    # logger.info(channel)
    # voice = get(bot.voice_clients, guild=ctx.guild)
    # logger.info(voice)
    # await channel.connect()
    # await ctx.send(f"Joined {channel}")
    # await ctx.send('ok')
    # await bot.join_voice_channel(ctx.message.author.voice)
    # discord.VoiceChannel.connect()
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    voice = await channel.connect()

    await ctx.send(f"Joined {channel}")


bot.run(os.environ['DISCORD_BOT_KEY'])