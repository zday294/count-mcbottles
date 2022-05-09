#bot.py
import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
PREFIX = '-'

class details:
    def __init__(self, pat, monitored, replace):
        self.pattern = pat
        self.monitoredChannel = monitored
        self.replaceChar = replace

deets = details("", None, "#")

bot = commands.Bot(PREFIX)


# COMMANDS
@bot.command(name='pattern', help="Sets the pattern for the selected channel")
async def pattern(ctx, *pat: str):
    pat = str.join(' ', pat)
    pattern = pat
    print("Setting pattern")
    print("\t", pattern)

@bot.command(name="setchannel", help="Set the bot's monitored channel to the current channel of the invoking user")
async def setchannel(ctx):
    deets.monitoredChannel = ctx.author.voice.channel
    print("Setting channel")
    print("\t", ctx.message.author)
    print("\t", ctx.author.voice.channel)
    print("\t", deets.monitoredChannel)

@bot.command(name='join', help="Join the voice channel the sending user is in")
async def join(ctx):
    # if(!message.member.voice.channel) return message.channel.send("Please connect to a voice channel!");
    channel = ctx.author.voice.channel
    print("Joining channel")
    print("\t",ctx.message.author)
    print("\t",ctx.author.voice.channel)
    await channel.connect()

@bot.command(name='leave', help="Banishes bot from the voice channel")
async def leave(ctx):
    print("leaving the vc")
    await ctx.voice_client.disconnect()


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

@bot.event
async def on_voice_state_update(member, before, after):
    print("Voice state update")
    print("\t", member)
    print("\tbefore.channel: ", before.channel)
    print("\tafter.channel: ", after.channel)
    print("\tmonitoredChannel: ", deets.monitoredChannel)
    if (deets.monitoredChannel == None):
        print("\tmonitoredChannel is null")
    elif (after.channel == deets.monitoredChannel):
        print("\tincrease number")
    elif (before.channel == deets.monitoredChannel):
        print("\tdecrease number")
    else:
        print("\thit the else")


# UTILS
async def getNumUsers():
    # get channel
    # get size of members property
    # https://stackoverflow.com/questions/66778544/get-count-of-users-in-a-voice-channel-discord-js
    for c in bot.get_all_channels:
        if c.id == deets.monitoredChannel.id:
            print("idk")
    print("not implemented")


def updateChannelName():
    numUsers = getNumUsers()
    update = pattern.replace(deets.replaceChar, str(numUsers))
    # update channel name here


def main():
    try:
        bot.run(TOKEN)
    except Exception as e:
        print("An expection occured; shutting down")


if __name__ == "__main__":
    main()