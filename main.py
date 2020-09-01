import discord, os
from discord.ext import commands

bot = commands.Bot(command_prefix='>')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

bot.run(os.getenv("DISCORD_TOKEN"))