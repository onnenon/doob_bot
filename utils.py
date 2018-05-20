import discord
from discord.ext import commands
from discord.ext.commands import Bot


def emify_info(em, wanted_items: list, **data):
    em.set_thumbnail(url=data.get('thumbnail_url'))
    for k, v in data.items():
        if not k.startswith('thumb') and k in wanted_items:

            if type(v) is dict:
                v_string = ''
                for key, value in v.items():
                    v_string += "{}: {}\n".format(
                        key.capitalize().replace("_", " "), value)
                em.add_field(name="{}".format(k.capitalize().replace(
                    "_", " ")), value=v_string, inline=True)

            elif type(v) is list:
                for item in v:
                    value_str = ""
                    for k, v in item.items():
                        if k in wanted_items:
                            value_str += "{}: {}\n".format(
                                k.capitalize().replace("_", " "), v)
                    em.add_field(name="++++++++++++++++++++++++",
                                 value=value_str, inline=False)

            else:
                em.add_field(name="{}:".format(k.capitalize().replace(
                    "_", " ")), value="{}".format(v), inline=True)

    return em
