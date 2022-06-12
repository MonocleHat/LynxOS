from discord.ext import commands
import os
import sys

class Admin(commands.Cog,name="Admin"):
    """Returns Admin information"""
    def __init__(self,bot:commands.Bot):
        self.bot = bot

    @commands.command()
    async def restart(self, ctx):
        await ctx.send("Restarting...")
        
        os.execv("LynxOS.py",sys.argv)

def setup(bot: commands.Bot):
    bot.add_cog(Admin(bot))