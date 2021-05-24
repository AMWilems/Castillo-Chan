import os
import discord

from dotenv import load_dotenv
from discord.ext import commands

load_dotenv("/home/pi/Documents/Callisto-Chan/.gitignore/.env")
name = "Kerbal Space Program"

bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    print('Logged in as {0.user}'.format(bot))#change from client to bot
    #await bot.change_presence(discord.Game(name))
    
@bot.command(name='hey')
async def hey(ctx):
    await ctx.channel.send('Hi everybody! ＼(^o^)／')

@bot.command(name='marco')
async def marco(ctx):
    await ctx.channel.send("Polo!")

@bot.command(name='shutdown')
async def shutdown(ctx):
    await ctx.channel.send("I'm gonna take a nap... Be back soon!")
    print("logging out..")
    await bot.close()
    print("logged out Successfully")
    
    
bot.run(os.getenv("TOKEN"))

#https://betterprogramming.pub/how-to-make-discord-bot-commands-in-python-2cae39cbfd55
#Inspiration to check out
#https://www.freecodecamp.org/news/create-a-discord-bot-with-python/
