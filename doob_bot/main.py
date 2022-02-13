from typing import Optional

import nextcord
from nextcord.ext import commands
from nextcord.ext.commands.context import Context

from doob_bot.embeds import get_char_info_embed
from doob_bot.raider_io.service import get_character_info
from doob_bot.settings import BOT_TOKEN, LOGGER

intents = nextcord.Intents.default()

BOT = commands.Bot(command_prefix="#", intents=intents)


@BOT.event
async def on_ready():
    """Prints to console when bot is running successfully."""
    LOGGER.info(f"{BOT.user.name} Is Running. ID: {BOT.user.id}")


@BOT.command()
async def info(ctx: Context, char_name: str, realm: str, region: Optional[str]):
    """When a message occurs, calls the handle message function"""
    LOGGER.info(f"{char_name} {realm} {region}")
    character_info = get_character_info(char_name, realm, region, ["gear", "guild"])
    embed = get_char_info_embed(character_info)
    await ctx.send(embed=embed)


@BOT.command()
async def ioscore(ctx: Context, name: str):
    pass


@BOT.command()
async def best(ctx: Context, name: str):
    pass


@BOT.command()
async def highest(ctx: Context, name: str):
    pass


if __name__ == "__main__":
    BOT.run(BOT_TOKEN)
