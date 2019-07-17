import discord
from discord.ext import commands

import datetime
import os

bot = commands.Bot(command_prefix=">", description="This is a basic bot")

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def sum(ctx, x: int, y: int):
    await ctx.send(x+y)

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
    await bot.change_presence(activity=discord.Streaming(name="Test", url="http://www.twitch.tv/account"))

bot.run(os.environ['DISCORD_BOT_KEY'])