import datetime

import nextcord
from nextcord.embeds import Embed

from doob_bot.models import BestRunData, CharacterInfoData, HighestRunData, IoscoreData


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


def add_dict_embed_field(em: Embed, k, v, inline=True) -> None:
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
        name=f"{k.capitalize().replace('_', ' ')}", value=v_string, inline=inline
    )


def get_char_info_embed(character_info: CharacterInfoData) -> Embed:
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


def get_ioscore_embed(ioscore_data: IoscoreData) -> Embed:
    embed = get_base_embed()

    embed.set_thumbnail(url=ioscore_data.thumbnail_url)
    embed.add_field(name="Name", value=ioscore_data.name)
    embed.add_field(name="Class", value=ioscore_data.class_.value)
    embed.add_field(name="Active Spec", value=ioscore_data.active_spec_name)
    embed.add_field(name="Realm", value=ioscore_data.realm)
    add_dict_embed_field(
        embed,
        "Mythic Plus Scores",
        ioscore_data.mythic_plus_scores.__dict__,
        inline=False,
    )

    return embed


def get_best_run_embed(best_run_data: BestRunData) -> Embed:
    # TODO
    embed = get_base_embed()

    embed.set_thumbnail(url=best_run_data.thumbnail_url)
    embed.add_field(name="Name", value=best_run_data.name)
    embed.add_field(name="Class", value=best_run_data.class_.value)
    embed.add_field(name="Active Spec", value=best_run_data.active_spec_name)
    embed.add_field(name="Realm", value=best_run_data.realm)
    return embed


def get_highest_run_embed(highest_run_data: HighestRunData) -> Embed:
    # TODO
    embed = get_base_embed()

    embed.set_thumbnail(url=highest_run_data.thumbnail_url)
    embed.add_field(name="Name", value=highest_run_data.name)
    embed.add_field(name="Class", value=highest_run_data.class_.value)
    embed.add_field(name="Active Spec", value=highest_run_data.active_spec_name)
    embed.add_field(name="Realm", value=highest_run_data.realm)
    return embed
