"""

Raider.io API info at https://raider.io/api#!/

"""

import json
import requests

from spylogger import get_logger

from doob_bot.exceptions import BadStatusCode
from doob_bot.utils import add_data_to_embed

LOGGER = get_logger(log_level="DEBUG")

API_URL_BASE = "https://raider.io/api/v1/"
HEADERS = {'Content-Type': 'application/json'}

DATA_LISTS = {
    "#info": [
        'name', 'class', 'active_spec_name', 'region', 'realm', 'faction',
        'gear', 'guild', 'profile_url', 'thumbnail_url'
    ],
    "#ioscore": [
        'name', 'realm', 'class', 'active_spec_name', 'mythic_plus_scores',
        'thumbnail_url', 'all', 'dps', 'healer', 'tank'
    ],
    "#best": [
        'name', 'class', 'active_spec_name', 'realm', 'mythic_plus_best_runs',
        'mythic_plus_highest_level_runs', 'dungeon', 'mythic_level',
        'num_keystone_upgrades', 'score', 'thumbnail_url'
    ],
    "#highest": [
        'name', 'class', 'active_spec_name', 'realm', 'mythic_plus_best_runs',
        'mythic_plus_highest_level_runs', 'dungeon', 'mythic_level',
        'num_keystone_upgrades', 'score', 'thumbnail_url'
    ]
}


def char_api_request(li: list, prefix: str, em):
    """Gets correct info from Raider.io API and returns correctly formatted
       Discord embed object.

    Args:
        li: The list of attributes that will be added to the embed object.
        prefix: Prefix the user passed to the bot in the message.
        em: The embed object that will have data added to it and then be
            returned.

    Raises:
        ValueError: If an invalid number of arguments are passed.
        Exception: If exception is thrown by get_character_info

    Returns:
        The embed object with all the fetched data correctly added.
    """
    try:
        if len(li) == 2:
            char_info = get_character_info(li[0], li[1], prefix)
        elif len(li) == 3:
            char_info = get_character_info(li[0], li[1], prefix, li[2])
        else:
            raise ValueError("Invalid number of arguments")
    except Exception as e:
        raise e

    return add_data_to_embed(em, DATA_LISTS.get(prefix), **char_info)


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
    FIELD_DATA = {
        '#info': ['gear', 'guild'],
        '#ioscore': ['mythic_plus_scores'],
        '#best': ['mythic_plus_best_runs'],
        '#highest': ['mythic_plus_highest_level_runs']
    }

    fields = []

    LOGGER.debug({"prefix": prefix})

    if prefix not in FIELD_DATA.keys():
        raise ValueError("Invalid Prefix")

    fields.extend(FIELD_DATA.get(prefix))

    LOGGER.debug({"Fields": fields})

    field_str = "&fields="
    for field in fields:
        field_str += f"{field}%2C"

    LOGGER.debug({"Field String Before": field_str})

    api_url = f"{API_URL_BASE}characters/profile?region={region}&realm={realm}&name={name}{field_str}"
    LOGGER.debug({"API URL": api_url})

    response = requests.get(api_url, headers=HEADERS)
    LOGGER.debug({"Status Code:": response.status_code})

    if response.status_code != 200 or response is None:
        raise BadStatusCode(
            "Bad response status code: " + str(response.status_code),
            status_code=response.status_code)

    r_content = json.loads(response.content)
    LOGGER.debug({"Response Content": r_content})
    return r_content
