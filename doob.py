# Doob the Discord Bot by onnenon

"""
 Invite Link https://discordapp.com/oauth2/authorize?client_id=<your_client_id>&scope=bot
"""

import asyncio
import datetime

import discord
from discord.ext import commands
from discord.ext.commands import Bot
from spylogger import get_logger

from raiderio_api import get_character
from utils import emify_info, pretty_string

from secrets import BOT_TOKEN


PREFIX_LIST = ['#info', '#ioscore']

bot = commands.Bot(command_prefix="#")

embed = discord.Embed(title="Doob Bot", colour=discord.Colour(0x52472b), url="https://discordapp.com",
                      description="A shitty Discord bot for getting Raider.io Data", timestamp=datetime.datetime.utcfromtimestamp(1526713815))


@bot.event
async def on_ready():
    print("{} Is Running".format(bot.user.name))
    print("With the ID: {}".format(bot.user.id))


@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say(":ping_pong: ping!!")


@bot.event
async def on_message(message):
    # Split the message into a list
    args = message.content.split(" ")

    # If first index of that list is in the defined prefixes prep the message
    if args[0] in PREFIX_LIST:
        prefix = args.pop(0)
        arg_fix = [arg.replace("_", " ") for arg in args]

        if len(arg_fix) == 2:
            user_info = get_character(arg_fix[0], arg_fix[1])

        elif len(arg_fix) == 3:
            user_info = get_character(arg_fix[0], arg_fix[1], arg_fix[2])

        # Gets character Info
        if prefix == '#info':
            if(user_info is not None):
                return await bot.send_message(message.channel, embed=emify_info(embed, **user_info))
            else:
                await bot.send_message(message.channel, "Error!")

        # Gets character IO Score
        if prefix == '#ioscore':
            if(user_info is not None):
                return await bot.send_message(message.channel, embed=emify_info(embed, **user_info))
            else:
                await bot.send_message(message.channel, "Error!")


bot.run(BOT_TOKEN)
