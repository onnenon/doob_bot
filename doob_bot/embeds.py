import datetime
from typing import List

import nextcord
from nextcord.embeds import Embed

from doob_bot.models import CharacterInfo


def get_base_embed() -> Embed:
    embed = Embed(
        title="Doob Bot",
        colour=nextcord.Colour(0x52472B),
        url="http://github.com/onnenon/doob_bot",
        description="A simple Discord bot for getting Raider.io Data\n",
        timestamp=datetime.datetime.now(),
    )
    embed.set_footer(text=("-" * 115))
    return embed


def add_dict_field(em: Embed, k, v) -> None:
    """Helper function to add dict to embed object with some formatting.

    Args:
        em: Embed object to add fields to.
        k: Key for the dict.
        v: The dict itself.
    """
    v_string = ""
    for key, value in v.items():
        v_string += f"{key.capitalize().replace('_', ' ')}: {value}\n"
    em.add_field(
        name=f"{k.capitalize().replace('_', ' ')}", value=v_string, inline=True
    )


def add_list_field(em: Embed, wanted_items: List[str], k: str, v: str) -> None:
    """Helper function to add list to embed object with some formatting.

    Args:
        em: Embed object to add fields to.
        k: The key for the list.
        v: The list itself.
    """
    for item in v:
        value_str = ""
        for k, v in item.items():
            if k in wanted_items:
                value_str += f"{k.capitalize().replace('_', ' ')}: {v}\n"
        em.add_field(name=("+" * 25), value=value_str, inline=False)


def get_char_info_embed(character_info: CharacterInfo) -> Embed:
    embed = get_base_embed()
    embed.set_thumbnail(url=character_info.thumbnail_url)
    embed.add_field(name="Name", value=character_info.name)
    embed.add_field(name="Class", value=character_info.class_.value)
    embed.add_field(name="Active Spec", value=character_info.active_spec_name)
    embed.add_field(name="Region", value=character_info.region.value)
    embed.add_field(name="Realm", value=character_info.realm)
    embed.add_field(name="Faction", value=character_info.faction.value)
    embed.add_field(
        name="Gear Score", value=character_info.gear.get("item_level_equipped")
    )
    embed.add_field(name="Guild", value=character_info.guild.name)
    embed.add_field(name="Profile Url", value=character_info.profile_url, inline=False)
    return embed
