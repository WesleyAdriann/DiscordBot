import discord
from discord.ext import commands
from discord.utils import get
import os
from urllib import parse, request
import re
from logger import logg


logger = logg('main_bot')

bot = commands.Bot(command_prefix = ">")

if not discord.opus.is_loaded():
    discord.opus.load_opus('opus')

logger.info('Starts Bot, waiting to be ready')

# EVENTOS
@bot.event
async def on_ready():
    logger.info(f'Bot {bot.user} is ready')
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
    logger.info(f"{ctx.guild.name} | {ctx.author} | {ctx.message.content}")
    embed = discord.Embed(
        title="Comandos",
        description="Todos os comandos começam com '>'",
        color=discord.Color.magenta(),
        )
    embed.add_field(name=">youtube pesquisa", value="Busca video no youtube //em construção")
    embed.add_field(name=">info", value="Exibe informações do servidor")
    embed.add_field(name=">limpar numero", value="Exclui quantidade de menssagens pelo numero passado")
    embed.add_field(name=">entrar", value="Entra no canal de voz")
    embed.add_field(name=">sair", value="Sai canal de voz")
    embed.set_thumbnail(url="https://cdn.discordapp.com/app-icons/600866134924984320/fe5bacc16fefd66e5c4690c2b12e2d16.png")
    await ctx.send(embed=embed)

@bot.command()
async def info(ctx):
    logger.info(f"{ctx.guild.name} | {ctx.author} | {ctx.message.content}")
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
    logger.info(f"{ctx.guild.name} | {ctx.author} | {ctx.message.content}")
    query_string = parse.urlencode({'search_query': search})
    html_content = request.urlopen('http://www.youtube.com/results?' + query_string)
    search_results = re.findall('href=\"\\/watch\\?v=(.{11})', html_content.read().decode())
    channel = ctx.author.voice
    await ctx.send('https://www.youtube.com/watch?v=' + search_results[0])



@bot.command()
async def limpar(ctx, amount : int):
    logger.info(f"{ctx.guild.name} | {ctx.author} | {ctx.message.content}")
    await ctx.channel.purge(limit=amount)

@limpar.error
async def limpar_error(ctx, error):
    logger.info(f"{ctx.guild.name} | {ctx.author} | {ctx.message.content}")
    if isinstance(err, commands.MissingRequiredArgument):
        await ctx.send('Informe a quantidade que deseja apagar.')


@bot.command()
async def entrar(ctx):
    logger.info(f"{ctx.guild.name} | {ctx.author} | {ctx.message.content}")
    voice = ctx.message.author.voice
    if voice is None:
        await ctx.send('Você não esta em um canal de voz.')
    elif ctx.voice_client is not None:
        if (str(voice.channel) == str(ctx.voice_client.channel)):
            await ctx.send(f'Ja estou conectado ao canal {str(voice.channel)}')
        else:
            await ctx.voice_client.move_to(voice.channel)
    else:
        voiceClient = voice.channel.connect()
        await voiceClient

@bot.command()
async def sair(ctx):
    await ctx.voice_client.disconnect()

@bot.command(pass_context=True)
async def test(ctx):
    logger.info('start test')
    methods = dir(ctx.voice_client.channel)
    # logger.info(ctx.bot)
    logger.info('methods')
    logger.info(methods)
    atts = vars(ctx.voice_client.channel) 
    logger.info(ctx.voice_client.channel)
    
    logger.info('atributes')
    logger.info(atts)


bot.run(os.environ['DISCORD_BOT_KEY'])