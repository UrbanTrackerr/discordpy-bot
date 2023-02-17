# This example requires the 'message_content' privileged intents

import os
import discord
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='>', intents=intents, self_bot =True)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send('i hate niggers')

@bot.command()
async def hello(ctx):
    await ctx.send("Choo choo! 🚅")

Cosmo = "NzM1NDE4NzU4Nzg4ODA4NzY2.GDfqTu.6UZJnKu9Yxwa52d8uHdynLIwCLXvtKXjPlTJnI"
bot.run(Cosmo)
