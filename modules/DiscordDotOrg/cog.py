from datetime import datetime
import time
from pytz import timezone
import pytz
from sqlite3 import Date
from discord.ext import commands
import discord
import json
import random
import os
#---------------
from sqlalchemy import Column
from sqlalchemy import text
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
    ChannelID = Column(Integer)

    def __repr__(self):
        return f"User(ID={self.ID!r}, Name={self.Name!r}, Msg={self.Msg!r},MsgDate={self.MsgDate!r})"

class DiscordDotOrg(commands.Cog, name="DiscordDotOrg"):
    """System of quotes to store user messages!"""
    @commands.command()
    async def quote(self,ctx:commands.Context, count:int,channel: discord.TextChannel=None):
        if count == 0:
            await ctx.send ("Usage <Command> <Count> (Count cannot be 0)")
        else:
            flag = True
            #Start
            session = Session(engine)
            stmt = session.query(UserMessage.ID).distinct(UserMessage.ID).count() #Count distinct ID's from user messages
            IDCOUNT=stmt 
            async for x in ctx.channel.history(limit=count+1):
                if flag == True:
                    print("Skipping message")
                    flag = False
                elif flag == False:
                    authorname = str(x.author).split("#")[0]
                    #set timezone to eastern
                    local_tz = pytz.timezone('US/Eastern')
                    timez = x.created_at.replace(tzinfo=pytz.utc).astimezone(local_tz)
                    quote_user = UserMessage(ID=IDCOUNT,Name=authorname, Msg = x.content, MsgDate=timez,ChannelID=ctx.guild.id)
                    session.add(quote_user)
            session.commit()

    @commands.command()
    async def recall(self,ctx:commands.Context):
        """Recall user messages, embeds for user display"""
        session = Session(engine)
        ids = session.execute(select(UserMessage.ID).distinct(UserMessage.ID).where(UserMessage.ChannelID==ctx.guild.id))
        #this gets a set of id's so that we can iterate over them
        #only the id's for a given channel are pulled
        channel_quotes=[]
        #store id's in an array for easy recalling later
        for row in ids:
            channel_quotes.append(row[0])
        search = random.choice(channel_quotes)

        #set up our embed 
        embed = discord.Embed(title="DiscordDotOrg",description="Remembering a quote...",color=0x00ffb3)
        stmt = select(UserMessage).where(UserMessage.ID == search).order_by(UserMessage.MsgDate) #SELECT * FROM USERMESSAGES WHERE ID = RANDOMIDVAL ORDER BY DATE
        with engine.connect() as conn:
            for row in conn.execute(stmt):
                unxtime = time.mktime(row.MsgDate.timetuple()) #convert time to unix time
                embed.add_field(name=f"{row.Name} -- <t:{int(unxtime)}:t>", value=row.Msg, inline=False)
        
        archivaldate = row.MsgDate.strftime("%d/%m/%Y")
        embed.set_footer(text=f"Archived On: {archivaldate}")
        session.rollback()
        await ctx.send(embed=embed)


def setup(bot: commands.Bot):
    bot.add_cog(DiscordDotOrg(bot))