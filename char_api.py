import discord
from discord.ext import commands
from discord.ext.commands import Bot

import utils
import raiderio_api
from utils import emify_info
from raiderio_api import get_character

INFO_DATA = ['name', 'class', 'active_spec_name', 'region',
             'realm', 'faction', 'profile_url', 'thumbnail_url']
IOSCORE_DATA = ['name', 'class', 'active_spec_name',
                'mythic_plus_scores', 'thumbnail_url', 'all', 'dps', 'healer', 'tank']
BEST_DATA = ['name', 'class', 'active_spec_name', 'mythic_plus_best_runs', 'mythic_plus_highest_level_runs', 'dungeon',
             'mythic_level', 'num_keystone_upgrades', 'score', 'thumbnail_url']


def char_api_request(li: list, prefix: str, em):
    if len(li) == 2:
        user_info = get_character(li[0], li[1], prefix)

    elif len(li) == 3:
        user_info = get_character(li[0], li[1], prefix, li[2])

    if(user_info is not None):
        # Gets character Info
        if prefix == '#info':
            return emify_info(em, INFO_DATA, **user_info)

        # Gets character IO Score
        if prefix == '#ioscore':
            return emify_info(em, IOSCORE_DATA, **user_info)

        if prefix == '#best' or prefix == '#highest':
            return emify_info(em, BEST_DATA, **user_info)

    return None
