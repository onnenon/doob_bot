"""

Raider.io API info at https://raider.io/api#!/

"""

import json
import requests

from spylogger import get_logger

from doob_bot.utils import emify_info

LOGGER = get_logger(log_level="DEBUG")

API_URL_BASE = "https://raider.io/api/v1/"
HEADERS = {'Content-Type': 'application/json'}

INFO_DATA = [
    'name', 'class', 'active_spec_name', 'region', 'realm', 'faction', 'gear', 'guild', 'profile_url', 'thumbnail_url'
]
IOSCORE_DATA = [
    'name', 'realm', 'class', 'active_spec_name', 'mythic_plus_scores', 'thumbnail_url', 'all', 'dps', 'healer', 'tank'
]
BEST_DATA = [
    'name', 'class', 'active_spec_name', 'realm', 'mythic_plus_best_runs', 'mythic_plus_highest_level_runs', 'dungeon',
    'mythic_level', 'num_keystone_upgrades', 'score', 'thumbnail_url'
]


def get_character_info(name: str, realm: str, prefix, region: str = "US"):
    """Returns Character Info from Raider.io

    Args:
        Name: Name of character.
        Realm: Realm of character.
        Prefix: Prefix or 'command' the user passed.
        Region: Region of character, defaults to US.

    Raises:
        Exception: If status code from API call is not 200.

    Returns:
        A dictionary containing all of the info from the API call
    """
    fields = []

    if prefix == '#info':
        fields.extend(('gear', 'guild'))
    elif prefix == '#ioscore':
        fields.append('mythic_plus_scores')
    elif prefix == '#best':
        fields.append('mythic_plus_best_runs')
    elif prefix == '#highest':
        fields.append('mythic_plus_highest_level_runs')

    field_str = ""
    if len(fields) > 0:
        field_str += "&fields="
        for field in fields:
            field_str += f"{field}%2C"

    if field_str.endswith("0"):
        field_str = field_str[:-3]

    api_url = f"{API_URL_BASE}characters/profile?region={region}&realm={realm}&name={name}{field_str}"

    response = requests.get(api_url, headers=HEADERS)

    if response.status_code != 200:
        raise Exception("Bad response status code: " + response.status_code)
        LOGGER.debug({"Status Code:": response.status_code})

    r_content = json.loads(response.content.decode('utf-8'))
    LOGGER.debug({"Response Content": r_content})
    return r_content


def char_api_request(li: list, prefix: str, em):
    """Gets correct info from Raider.io API and returns correctly formatted Discord embed object.

    Args:
        li: The list of attributes that will be added to the embed object.
        prefix: Prefix the user passed to the bot in the message.
        em: The embed object that will have data added to it and then be returned.

    Raises:
        ValueError: If an invalid number of arguments are passed.
        Exception: If exception is thrown by get_character_info

    Returns:
        The embed object with all the fetched data correctly added.
    """
    try:
        if len(li) not in range(2, 4):
            raise ValueError("Invalid number of arguments")

        if len(li) == 2:
            user_info = get_character_info(li[0], li[1], prefix)

        elif len(li) == 3:
            user_info = get_character_info(li[0], li[1], prefix, li[2])

    except Exception as e:
        raise e

    # Gets a character's Info
    if prefix == '#info':
        return emify_info(em, INFO_DATA, **user_info)

    # Gets a character's IO Score
    if prefix == '#ioscore':
        return emify_info(em, IOSCORE_DATA, **user_info)

    # Gets a character's "best" or "highest" Mythic+ runs
    if prefix == '#best' or prefix == '#highest':
        return emify_info(em, BEST_DATA, **user_info)
