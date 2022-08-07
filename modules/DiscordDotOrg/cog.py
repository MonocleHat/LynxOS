from datetime import datetime
from sqlite3 import Date
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
    MsgDate=Column(sqlalchemy.DateTime)

    def __repr__(self):
        return f"User(ID={self.ID!r}, Name={self.Name!r}, Msg={self.Msg!r},MsgDate={self.MsgDate!r})"

class DiscordDotOrg(commands.Cog, name="DiscordDotOrg"):
    """System of quotes to store user messages!"""
    @commands.command()
    async def quoteme(self,ctx:commands.Context, count:int,channel: discord.TextChannel=None):
        if count == 0:
            await ctx.send ("Usage <Command> <Count> (Count cannot be 0)")
        else:
            flag = True
            #Start
            session = Session(engine)
            stmt = session.query(UserMessage.ID).distinct(UserMessage.ID).count()
            IDCOUNT=stmt 
            async for x in ctx.channel.history(limit=count+1):
                if flag == True:
                    print("Skipping message")
                    flag = False
                elif flag == False:
                    authorname = str(x.author).split("#")[0]
                    quoteUser = UserMessage(ID=IDCOUNT,Name=authorname, Msg = x.content, MsgDate=x.created_at)
                    session.add(quoteUser)
                    print(quoteUser)
            session.commit()

    @commands.command()
    async def quoteme(self,ctx:commands.Context):
        """Recall user messages, embeds for user display"""
        # Steps
        # Retrieve count of items
        # If count is < 1 - display "Error: No Quotes Stored - use $quoteme <value> to store text"
        # if count is > 1 - generate a random number between 0-the max count
        # store each instance of the object in an array
        # create an embed object and slowly fill it with the quotes from each user in the following format
        # Date of Conversation
        # Message Author // Message 
        # To retrieve messages use
        # SELECT * FROM <TABLE> WHERE ID = <Generated Number> ORDER BY <COL 4>
        await ctx.send("Not yet implemented")

def setup(bot: commands.Bot):
    bot.add_cog(DiscordDotOrg(bot))