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
        self.rstr = None

        #loading our data into our objects
        with open(os.path.join(os.path.dirname(__file__),"lynxes.json")) as lnx:
            self.lynx = json.load(lnx)

        with open(os.path.join(os.path.dirname(__file__),"yeens.json")) as yen:
            self.yeen = json.load(yen)

        with open(os.path.join(os.path.dirname(__file__), "chi.json")) as ch:
            self.chi = json.load(ch)
        with open("restricted.json") as rstr:
            self.rstr = json.load(rstr)
    @commands.command()
    async def animal(self,ctx: commands.Context,type:str):
        """Gets an animal and displays corresponding picture"""
        flag = False
        for x in self.rstr:
            print(self.rstr[x])
            if str(ctx.guild.id) == str(self.rstr[x]):
                print("BANNED OR RESTRICTED GUILD DETECTED")
                flag = True
                print("Command Disabled Here")
                await ctx.send("This command may be disabled or an incorrect value was sent")
        if type == "lynx" and flag == False:
            print("Fetching Lynx")
            choice = random.randint(0,len(self.lynx.keys()))
            retval = self.lynx[str(choice)]
            await ctx.send(retval)
        elif type == "yeen" and flag == False:

            print("Fetching Yeen")
            choice = random.randint(0,len(self.yeen.keys()))
            retval = self.yeen[str(choice)]
            await ctx.send(retval)
        elif type == "chi" and flag == False:
            print("Fetching Chi")
            choice = random.randint(0,len(self.chi.keys()))
            retval = self.chi[str(choice)]
            await ctx.send(retval)
def setup(bot: commands.Bot):
    bot.add_cog(Animal(bot))