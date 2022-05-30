#bot.py
import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
import persistBot
from details import Details

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
JSON_FILE = os.getenv('JSON_FILE')

# deets = Details("", None, "#", '-')

bot = persistBot.PersistBot(JSON_FILE)


# COMMANDS
@bot.command(name='pattern', help="Sets the pattern for the selected channel")
async def pattern(ctx, *pat: str):
    pat = str.join(' ', pat)
    bot.details.pattern = pat
    print("Setting pattern")
    await showpattern(ctx)
    print("\t", pattern)

@bot.command(name="setchannel", help="Set the bot's monitored channel to the current channel of the invoking user")
async def setchannel(ctx):
    bot.details.monitoredChannel = ctx.author.voice.channel
    bot.details.number = getNumUsers(bot.details.monitoredChannel)
    print("Setting channel")
    print("\t", ctx.message.author)
    print("\t", ctx.author.voice.channel)
    print("\t", bot.details.monitoredChannel)
    print("\tMembers connected: ", bot.details.number)

@bot.command(name="showpattern", help="Sends a message showing the current pattern")
async def showpattern(ctx):
    await ctx.send(f'The current pattern is "{bot.details.pattern}"')
    # print("hello")

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
    print("\tmonitoredChannel: ", bot.details.monitoredChannel)
    if (deets.monitoredChannel == None):
        print("\tmonitoredChannel is null")
    elif (after.channel == bot.details.monitoredChannel):
        print("\tincrease number")
        deets.number += 1
    elif (before.channel == bot.details.monitoredChannel):
        print("\tdecrease number")
        deets.number -= 1
    else:
        print("\thit the else")
    print("\tdeets.number: ", bot.details.number)
    await updateChannelName()


# UTILS
def getNumUsers(channel):
    return len(channel.members)


async def updateChannelName():
    numUsers = bot.details.number
    update = pattern.replace(bot.details.replaceChar, str(numUsers))
    await bot.details.monitoredChannel.edit(name=update)
    # update channel name here


def main():
    try:
        bot.run(TOKEN)
    except Exception as e:
        print("An expection occured; shutting down")


if __name__ == "__main__":
    main()