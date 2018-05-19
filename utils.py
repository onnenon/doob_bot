import discord
from discord.ext import commands
from discord.ext.commands import Bot

IO_SCORE_ITEMS = ['name', 'class',
                  'active_spec_roll', 'gear', 'mythic_plus_scores', 'profile_url']


def pretty_string(*args, **kwargs):
    str = ""
    for k, v in kwargs.items():
        if not k.startswith('thumb'):
            if k == "name":
                str += "==============================\n"
                str += "Raider.io Info for {}\n".format(v)
                str += "==============================\n\n"
            elif k == "mythic_plus_scores":
                str += "io score: {}\n\n".format(v.get('all'))
            else:
                str += "{}: {}\n\n".format(k.capitalize().replace("_", " "), v)

    return str


def emify_info(em, **data):
    em.set_image(url=data.get('thumbnail_url'))
    for k, v in data.items():
        if not k.startswith('thumb') and not k.startswith('profile'):
            em.add_field(name="{}:".format(k.capitalize().replace(
                "_", " ")), value="{}".format(v), inline=True)

    return em


def emify_ioscore(em, **data):
    em.set_image(url=data.get('thumbnail_url'))
    for k, v in data.items():
        if not k.startswith('thumb') and not k.startswith('profile'):
            em.add_field(name="{}:".format(k.capitalize().replace(
                "_", " ")), value="{}".format(v), inline=True)

    return em
