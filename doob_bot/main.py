from typing import Optional

import nextcord
from nextcord.ext import commands
from nextcord.ext.commands.context import Context

from doob_bot.embeds import (
    get_best_run_embed,
    get_char_info_embed,
    get_highest_run_embed,
    get_ioscore_embed,
)
from doob_bot.models import CommandCharacterData
from doob_bot.raider_io.service import (
    get_best_run_data,
    get_character_info_data,
    get_highest_run_data,
    get_ioscore_data,
)
from doob_bot.settings import BOT_TOKEN, LOGGER

intents = nextcord.Intents.default()

BOT = commands.Bot(command_prefix="#", intents=intents)


@BOT.event
async def on_ready():
    """Prints to console when bot is running successfully."""
    LOGGER.info(f"{BOT.user.name} Is Running. ID: {BOT.user.id}")


@BOT.command()
async def info(ctx: Context, char_name: str, realm: str, region: Optional[str]):
    try:
        LOGGER.info(f"{char_name} {realm} {region}")
        character_info = get_character_info_data(
            CommandCharacterData(char_name, realm, region)
        )
        embed = get_char_info_embed(character_info)
        await ctx.send(embed=embed)
    except Exception as e:
        LOGGER.error(e)
        await ctx.send("Oops, something happened")


@BOT.command()
async def ioscore(ctx: Context, char_name: str, realm: str, region: Optional[str]):
    try:
        LOGGER.info(f"{char_name} {realm} {region}")
        ioscore_info = get_ioscore_data(CommandCharacterData(char_name, realm, region))
        embed = get_ioscore_embed(ioscore_info)
        await ctx.send(embed=embed)
    except Exception as e:
        LOGGER.error(e)
        await ctx.send("Oops, something happened")


@BOT.command()
async def best(ctx: Context, char_name: str, realm: str, region: Optional[str]):
    try:
        LOGGER.info(f"{char_name} {realm} {region}")
        best_run_data = get_best_run_data(
            CommandCharacterData(char_name, realm, region)
        )
        embed = get_best_run_embed(best_run_data)
        await ctx.send(embed=embed)
    except Exception as e:
        LOGGER.error(e)
        await ctx.send("Oops, something happened")


@BOT.command()
async def highest(ctx: Context, char_name: str, realm: str, region: Optional[str]):
    try:
        LOGGER.info(f"{char_name} {realm} {region}")
        highest_run_data = get_highest_run_data(
            char_name, realm, region, ["gear", "guild"]
        )
        embed = get_highest_run_embed(highest_run_data)
        await ctx.send(embed=embed)
    except Exception as e:
        LOGGER.error(e)
        await ctx.send("Oops, something happened")


if __name__ == "__main__":
    BOT.run(BOT_TOKEN)
