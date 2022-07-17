from discord.ext import commands
import discord
import json
import random
import os
#---------------
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String 
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy import func
from sqlalchemy.orm import Session
from sqlalchemy import select
import sqlalchemy
import sqlalchemy.orm
#---------------
#Create Engine to connect to our database
engine = create_engine("sqlite:///LynxOS.db",echo=True,future=True)
Base = declarative_base()
#User Table
class UserMessage(Base):
    __tablename__ = "UserMessages"
    ID = Column(Integer,primary_key=True)
    Name=Column(String(30))
    Msg=Column(String)
    MsgDate=Column(String)

    def __repr__(self):
        return f"User(ID={self.ID!r}, Name={self.Name!r}, Msg={self.Msg!r},MsgDate={self.MsgDate!r})"

class DiscordDotOrg(commands.Cog, name="DiscordDotOrg"):
    """System of quotes to store user messages!"""
    @commands.command()
    async def quoteme(self,ctx:commands.Context, count:int,channel: discord.TextChannel=None):
        if count == 0:
            await ctx.send("PARAMETER CANNOT BE 0")
        else:
            
            flag = True
            
            async for x in ctx.channel.history(limit=count+1):
                if flag == True:
                    print("Skipping User Message")
                    flag = False
                elif flag == False:
                    obj = x.created_at
                    authorname = str(x.author).split("#")[0]
                    print(authorname)
                    obredone = str(obj)
                    print(obredone)
                    session = Session(engine)
                    # RES= session.execute("SELECT COUNT(DISTINCT ID) FROM UserMessages")
                    # print(RES.first()[0])
                        
                    stmt = session.query(UserMessage.ID).distinct(UserMessage.ID).count()
                    check = stmt
                    print(check)
                    await ctx.send(f'Author: {authorname}, Message: {x.content}, Sent on: {obj}')
            

        # async for x in ctx.channel.history(limit = count):
        #     print(x.author)
        #     print(x.content)
        #     obj = x.created_at
        #     print("Created at: ")
        #     print(obj)
        #     print("______")
        #     #await ctx.send(f'Author: {x.author}, Message: {x.content}, Sent on: {obj}')
        #     await ctx.send(x.content)


def setup(bot: commands.Bot):
    bot.add_cog(DiscordDotOrg(bot))