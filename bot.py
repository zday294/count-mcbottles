#bot.py
from cmath import e
import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
PREFIX = '-'

pattern = ""


bot = commands.Bot(PREFIX)


# COMMANDS
@bot.command(name='pattern', help="Sets the pattern for the selected channel")
async def pattern(ctx, *pat: str):
    pat = str.join(' ', pat)
    pattern = pat
    print(pattern)

@bot.command(name='join', help="Join the voice channel the sending user is in")
async def join(ctx):
    
    print(ctx.message.author)


# EVENTS 
@bot.event
async def on_error(events, *args, **kwargs):
    print("Exception occurred")
    print("\t", events)
    print("\t", args)
    print("\t", kwargs)


@bot.event
async def on_ready():
    for guild in bot.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{bot.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')


# UTILS
async def get_users():
    #get channel
    #get size of members property
    #https://stackoverflow.com/questions/66778544/get-count-of-users-in-a-voice-channel-discord-js
    print("not implemented")

def main():
    try:
        bot.run(TOKEN)
    except Exception as e:
        print("An expection occured; shutting down")


if __name__ == "__main__":
    main()