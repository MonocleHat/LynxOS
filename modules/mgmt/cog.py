from discord.ext import commands
import discord
import os
import sys

class Admin(commands.Cog,name="Admin"):
    """Returns Admin information"""
    def __init__(self,bot:commands.Bot):
        self.bot = bot

    @commands.command()
    async def restart(self, ctx):
        """Restart the bot to load any changes on the fly -- restarts it across the board -- INSECURE"""
        await ctx.send("Restarting...")
        
        os.execv("LynxOS.py",sys.argv)

    @commands.command()
    async def assist(self,ctx):
        """Display an embedded list of help stuff"""
        embed= discord.Embed(title="Command List", color=discord.Color(0x3acce7),description="Below is a list of commands that can be run here")
        embed.set_author(name="LynxOS - Console -- V2 -- Updated: June 2022",
                     icon_url="https://cdn.discordapp.com/attachments/740683821288128574/742397485661552800/photo_2020-07-25_19-00-23.jpg")
        embed.add_field(name="\nHow to use the commands",
                    value="prefix all commands with \'$\'\n", inline=False)
        embed.add_field(
        name="\nList", value="various commands include animal,memes,nick,speak,connect,now_playing,pause,play,queue,resume,skip,stop,volume,help,assist\n some of these are disabled for now", inline=False)
    #VERSION 2.0

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(Admin(bot))