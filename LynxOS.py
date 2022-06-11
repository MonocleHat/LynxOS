#!/bin/env python3
import discord
import random
import json
import sys
import os
import discord
from discord.ext import commands
# Music Bot Packages
import asyncio
import traceback
import itertools
from functools import partial
from async_timeout import timeout
from youtube_dl import YoutubeDL


# Importing our modules
with open('memes.json','r') as f:
    memes = json.load(f)

with open('token.json','r') as x:
    TOKEN_FILE = json.load(x)

with open('nicks.json','r') as n:
    nick = json.load(n)

with open('yeens.json','r') as y:
    yeens = json.load(y)

with open('lynxes.json','r') as l:
    lynxes = json.load(l)

with open('chi.json','r') as c:
    chis = json.load(c)

with open('responses.json','r') as r:
    responses = json.load(r)

TOKEN = TOKEN_FILE["token"]
randomSpeak = 0
client = commands.Bot(command_prefix = '$') # '$' triggers commands



@client.command()
async def ping(ctx):
    await ctx.send("Pong!")

@client.command()
async def speak(ctx):
    choice = random.randint(0,len(responses.keys()))
    retval = responses[str(choice)]
    print(retval)
    await ctx.send(retval)

@client.command()
async def lonx(ctx):
    choice = random.randint(0,len(lynxes.keys()))
    retval = lynxes[str(choice)]
    await ctx.send(retval)

@client.command(pass_context=True)
async def nick(ctx, member: discord.Member):
    await ctx.send('Spinning the fuckin nickname wheel,boyo')
    choice = random.randint(0,len(nick.keys()))
    retval = nick[str(choice)]
    await member.edit(nick=retval)
    await ctx.send(f'Nickname changed for {member.mention}')

@client.command()
async def yeen(ctx):
    choice = random.randint(0,len(yeens.keys()))
    retval = yeens[str(choice)]
    await ctx.send(retval)

@client.command()
async def restart(ctx):
    await ctx.send("Restarting...")
    os.execv(__file__,sys.argv)

@client.command()
async def chi(ctx):
    choice = random.randint(0,len(chis.keys()))
    retval = chis[str(choice)]
    await ctx.send(retval)

@client.command()
async def assist(ctx):
    
    embed= discord.Embed(title="Command List", color=discord.Color(0x3acce7),description="Below is a list of commands that can be run here")
    embed.set_author(name="LynxOS - Console -- V2 -- Updated: June 2022",
                     icon_url="https://cdn.discordapp.com/attachments/740683821288128574/742397485661552800/photo_2020-07-25_19-00-23.jpg")
    embed.add_field(name="\nHow to use the commands",
                    value="prefix all commands with \'$\'\n", inline=False)
    embed.add_field(
        name="\nList", value="ping = returns \'pong\'\nspeak = returns a random quote\nassist = display this list", inline=False)
    #VERSION 2.0
    embed.add_field(name="\nAnimal Pics",
                    value="use command prefix + either \'lonx\', \'chi\', or \'yeen\' to post a randomly selected picture of a lynx, a awd or a hyena", inline=False)
    embed.add_field(name="\nAuto-triggered keywords",
                    value=list(memes.keys()), inline=False)
    
    await ctx.send(embed=embed)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content in memes:
        msg = memes[message.content]
        
        # DEBUG print(msg)
        #await message.channel.send(msg)
        await message.channel.send(msg)
    await client.process_commands(message)

@client.event
async def on_ready():
    general_channel = client.get_channel(984950680726937600)
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    bot_message = "LynxOS Online, OS Version 2\n use $assist to view commands\nThis version is currently running off my main system and not the bot server, its only up for testing atm"
    await general_channel.send(bot_message)
    print("READY")

# Constructing the music portion



client.run(TOKEN)
