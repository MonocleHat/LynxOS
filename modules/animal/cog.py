from discord.ext import commands
import json
import random
import os

class Animal(commands.Cog, name="Animal"):
    """Returns an animal
    Syntax: $Animal <animal type here>
    """
    def __init__(self,bot:commands.Bot):
        self.bot = bot
        self.lynx = None
        self.yeen = None
        self.chi = None

        #loading our data into our objects
        with open(os.path.join(os.path.dirname(__file__),"lynxes.json")) as lnx:
            self.lynx = json.load(lnx)

        with open(os.path.join(os.path.dirname(__file__),"yeens.json")) as yen:
            self.yeen = json.load(yen)

        with open(os.path.join(os.path.dirname(__file__), "chi.json")) as ch:
            self.chi = json.load(ch)
        
    @commands.command()
    async def animal(self,ctx: commands.Context,type:str):
        """Gets an animal and displays corresponding picture"""
        
        if type == "lynx":
            print("Fetching Lynx")
            choice = random.randint(0,len(self.lynx.keys()))
            retval = self.lynx[str(choice)]
            await ctx.send(retval)
        elif type == "yeen":
            print("Fetching Yeen")
            choice = random.randint(0,len(self.yeen.keys()))
            retval = self.yeen[str(choice)]
            await ctx.send(retval)
        elif type == "chi":
            print("Fetching Chi")
            choice = random.randint(0,len(self.chi.keys()))
            retval = self.chi[str(choice)]
            await ctx.send(retval)

def setup(bot: commands.Bot):
    bot.add_cog(Animal(bot))