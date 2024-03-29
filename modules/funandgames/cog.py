from discord.ext import commands
import discord
import json
import random
import os

class FunAndGames(commands.Cog, name="FunAndGames"):
    """Varying Fun and Games"""
    def __init__(self,bot:commands.Bot):
        self.bot = bot
        self.responses = None #stores data from responses file
        self.memes = None
        self.nicks = None
        self.rstr = None

        #loads our data
        with open(os.path.join(os.path.dirname(__file__),"responses.json")) as res:
            self.responses = json.load(res)
        
        with open(os.path.join(os.path.dirname(__file__),"memes.json")) as mem:
            self.memes = json.load(mem)

        with open(os.path.join(os.path.dirname(__file__),"nicks.json")) as nik:
            self.nicks = json.load(nik)

        with open("restricted.json") as rstr:
            self.rstr = json.load(rstr)

    @commands.command()
    async def memes(self,ctx:commands.Context,srch:str):
        """Gets a meme from collection of memes"""
        if srch == "dumpall":
            await ctx.send(self.memes.keys())
        else:   
            print ("Fetching a meme: " + srch)
            retval = self.memes[srch]
            await ctx.send(retval)

    @commands.command()
    async def speak(self,ctx:commands.Context):
        """Returns a random quote to speak to a user"""
        flag = False
        for x in self.rstr:
            print(self.rstr[x])
            if str(ctx.guild.id) == str(self.rstr[x]):
                print("BANNED OR RESTRICTED GUILD DETECTED")
                flag = True
                print("Command Disabled Here")
                await ctx.send("This command may be disabled or an incorrect value was sent")
        if flag == False:
            print("Speaking the truth")
            choice = random.randint(0,len(self.responses.keys()))
            retval = self.responses[str(choice)]
        await ctx.send(retval)

    @commands.command()
    async def nick(self,ctx:commands.Context, member: discord.Member):
        """Returns a new nickname -- BROKEN"""
        await ctx.send("Command Disabled as Nickname Setting is still buggy. Sorry :p")
        # choice = random.randint(0,len(self.nicks.keys()))
        # retval = self.nicks[str(choice)]
        # await member.edit(nick=retval)
        # await ctx.send(f'Nickname changed: {member.mention}')

def setup(bot: commands.Bot):
    bot.add_cog(FunAndGames(bot))
