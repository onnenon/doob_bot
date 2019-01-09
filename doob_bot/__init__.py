"""
 Doob Bot, A simple discord bot for Raider.io

 Author: Stephen Onnen

 Github: https://github.com/onnenon/doob_bot

"""

import os

from discord.ext import commands

from doob_bot.handler import handle_message
from doob_bot.settings import LOGGER

BOT_TOKEN = os.getenv('BOT_TOKEN')

BOT = commands.Bot(command_prefix="#")


@BOT.event
async def on_ready():
    """Prints to console when bot is running successfully. """
    LOGGER.info(f"{BOT.user.name} Is Running. ID: {BOT.user.id}")


@BOT.event
async def on_message(message):
    """When a message occurs, calls the handle message function"""

    LOGGER.debug({"Message content": message.content})
    try:
        em = handle_message(message)
        if em is not None:
            await message.channel.send(embed=em)
    except ValueError as e:
        LOGGER.error({"Exception:": str(e)})
        await message.channel.send("Invalid number of arguments!")
    except Exception as e:
        LOGGER.error({"Exception:": str(e)})
        await message.channel.send(
            "No data was returned from Raider.io, check your spelling!!")


if __name__ == "__main__":
    BOT.run(BOT_TOKEN)
