#!/bin/env python3

#base imports
import discord
import json
import os
from discord.ext import commands

#config our main function
def main():
    client = commands.Bot(command_prefix="$")

    @client.event
    async def on_ready():
        print(f"{client.user.name} has logged in")
        tester_channel = client.get_channel(984950680726937600)
        await tester_channel.send("LynxOS Rewrite Online")

    for folder in os.listdir("modules"):
        if os.path.exists(os.path.join("modules",folder,"cog.py")):
            client.load_extension(f"modules.{folder}.cog")
    
    with open('token.json','r') as tok:
        TOKEN_FILE = json.load(tok)

    client.run(TOKEN_FILE["token"])


if __name__ == '__main__':
    main()