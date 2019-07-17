import discord
from discord.ext import commands

import datetime
import os

bot = commands.Bot(command_prefix=">", description="This is a basic bot")

@bot.command()
async def ajuda(ctx):
    embed = discord.Embed(
        title="Comandos",
        description="Todos os comandos começam com '>'",
        color=discord.Color.magenta(),
        )
    embed.add_field(name=">youtube valor", value="Busca video no youtube")
    embed.set_thumbnail(url="https://cdn.discordapp.com/app-icons/600866134924984320/fe5bacc16fefd66e5c4690c2b12e2d16.png")
    await ctx.send(embed=embed)

@bot.command()
async def info(ctx):
    embed = discord.Embed(
        title=f"{ctx.guild.name}",
        description="HUE",
        timestamp=datetime.datetime.utcnow(),
        color=discord.Color.blue()
        )
    embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Server owner", value=f"{ctx.guild.owner}")
    embed.add_field(name="Server region", value=f"{ctx.guild.region}")
    embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
    embed.set_thumbnail(url="https://techcrunch.com/wp-content/uploads/2018/07/logo-2.png")
    await ctx.send(embed=embed)

@bot.command()
async def youtube(ctx, *, search):
    query_string = parse.urlencode({'search_query' : search})
    html_content = request.urlopen(f"http://www.youtube.com/results?{query_string}")
    re.findall("href=\\/watch\\?v=(.{11})")
     
@bot.event
async def on_ready():
    activity = discord.Activity(
        name=">ajuda",
        type=discord.ActivityType.listening,
        )
    await bot.change_presence(activity=activity,)

bot.run(os.environ['DISCORD_BOT_KEY'])