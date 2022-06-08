#!/bin/env python3
import discord
import random
import json
import sys
import os
from discord.ext import commands

# Importing our modules
with open('memes.json','r') as f:
    memes = json.load(f)
with open('token.json','r') as x:
    TOKEN_FILE = json.load(x)

for x in memes:
    print(memes[x])
    print(memes.keys())

TOKEN = TOKEN_FILE["token"]
randomSpeak = 0
client = commands.Bot(command_prefix = '$') # '$' triggers commands


@client.command()
async def ping(ctx):
    await ctx.send("Pong!")

@client.command()
async def speak(ctx):
    response = random.choice(responses)
    print(response)
    await ctx.send(response)

@client.command()
async def lonx(ctx):
    lynx_selection = random.choice(lynxes)
    await ctx.send(lynx_selection)

@client.command(pass_context=True)
async def nick(ctx, member: discord.Member):
    await ctx.send('Spinning the fuckin nickname wheel,boyo')
    newnick = random.choice(nicks)
    await member.edit(nick=newnick)
    await ctx.send(f'Nickname changed for {member.mention}')

@client.command()
async def yeen(ctx):
    yeen_selection = random.choice(yeens)
    await ctx.send(yeen_selection)

@client.command()
async def recurserecurse(ctx):
    await ctx.send("RECURSE RECURSE!")
    os.execv(__file__,sys.argv)

@client.command()
async def chi(ctx):
    chi_selection = random.choice(chis)
    await ctx.send(chi_selection)

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
    # general_channel = client.get_channel(<testing channel here>)
    # print('Logged in as')
    # print(client.user.name)
    # print(client.user.id)
    # bot_message = "LynxOS Online, OS Version 2\n use $assist to view commands\nThis version is currently running off my main system and not the bot server, its only up for testing atm"
    # await general_channel.send(bot_message)
    print("READY")

    

client.run(TOKEN)
