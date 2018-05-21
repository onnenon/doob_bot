# Doob the Discord Bot by onnenon

"""
 Invite Link https://discordapp.com/oauth2/authorize?client_id=<your_client_id>&scope=bot
"""

import asyncio
import datetime
import time
import copy

import discord
from discord.ext import commands
from discord.ext.commands import Bot

from raiderio_api import char_api_request

from secrets import BOT_TOKEN


CHAR_PREFIX = ['#info', '#ioscore', '#best', '#highest']
MYTHIC_PLUS_PREFIX = []

bot = commands.Bot(command_prefix="#")

embed = discord.Embed(title="Doob Bot", colour=discord.Colour(0x52472b), url="https://discordapp.com",
                      description="A shitty Discord bot for getting Raider.io Data\n", timestamp=datetime.datetime.utcfromtimestamp(time.time()))
embed.set_footer(
    text=("-" * 115))


@bot.event
async def on_ready():
    print("{} Is Running".format(bot.user.name))
    print("With the ID: {}".format(bot.user.id))


@bot.event
async def on_message(message):
    # Split the message into a list
    args = message.content.split(" ")

    # If first index of that list is in the defined prefixes prep the message
    if args[0] in CHAR_PREFIX or args[0] in MYTHIC_PLUS_PREFIX:
        prefix = args.pop(0)
        arg_fix = [arg.replace("_", "-") for arg in args]

        if prefix in CHAR_PREFIX:
            try:
                em = char_api_request(arg_fix, prefix, copy.copy(embed))
                return await bot.send_message(message.channel, embed=em)
            except:
                return await bot.send_message(message.channel, "No data was returned from Raider.io, check your spelling!!")

        if prefix in MYTHIC_PLUS_PREFIX:
            pass


bot.run(BOT_TOKEN)
