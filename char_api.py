import discord
from discord.ext import commands
from discord.ext.commands import Bot

import utils
import raiderio_api
from utils import emify_info
from raiderio_api import get_character


def char_api_request(li: list, prefix: str, em):
    if len(li) == 2:
        user_info = get_character(li[0], li[1])

    elif len(li) == 3:
        user_info = get_character(li[0], li[1], li[2])

    if(user_info is not None):
        # Gets character Info
        if prefix == '#info':
            return emify_info(em, **user_info)

        # Gets character IO Score
        if prefix == '#ioscore':
            return emify_info(em, **user_info)
    return None
