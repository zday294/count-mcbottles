#bot.py
import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
PREFIX = '-'



client = discord.Client()

@commands.command()
async def pattern(pat: str):
    print(pat)




async def get_users():
    #get channel
    #get size of members property
    #https://stackoverflow.com/questions/66778544/get-count-of-users-in-a-voice-channel-discord-js
    print("not implemented")

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

client.run(TOKEN)