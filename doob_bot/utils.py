"""
Utility functions for doob_bot.
"""
from doob_bot.settings import LOGGER


def add_dict_field(em, k, v):
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


def add_list_field(em, wanted_items: list, k, v):
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


def add_normal_field(em, k, v):
    """Helper function to add a k, v to an embed object with some formatting.

    Args:
        em: Embed object to add fields to.
        k: The key to be added.
        v: The value to be added.
    """
    em.add_field(name=f"{k.capitalize().replace('_', ' ')}:", value=f"{v}", inline=True)


def add_data_to_embed(em, wanted_items: list, **data):
    """Takes given embed object and data, and adds the data to the embed object.

    Args:
        em: Embed object to add formatted data to.
        wanted_items: List of 'Keys' to be pulled from data and added to embed.
        data: Dictionary returned from the Raider.io API call.

    Returns:
        Embed object with all "wanted" data correctly added to it.
    """
    em.set_thumbnail(url=data.get("thumbnail_url"))
    LOGGER.debug({"Thumbnail URL": data.get("thumbnail_url")})
    for k, v in data.items():
        if not k.startswith("thumb") and k in wanted_items:
            if type(v) is dict:
                add_dict_field(em, k, v)
            elif type(v) is list:
                add_list_field(em, wanted_items, k, v)
            else:
                add_normal_field(em, k, v)
    return em
