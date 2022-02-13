"""
Raider.io API info at https://raider.io/api#!/
"""
import json
from typing import List, Optional

import requests

from doob_bot.models import CharacterInfo
from doob_bot.settings import LOGGER

API_URL_BASE = "https://raider.io/api/v1/"
HEADERS = {"Content-Type": "application/json"}


def get_character_info(
    char_name: str,
    realm: str,
    region: str,
    fields: Optional[List[str]],
):
    field_str = get_query_string_for_fields_list(fields)
    url = f"{API_URL_BASE}characters/profile?region={region}&realm={realm}&name={char_name}{field_str}"  # noqa: E501

    LOGGER.debug(url)

    response = requests.get(url, headers=HEADERS)
    response_json = json.loads(response.text)
    LOGGER.debug(response_json)

    character_info = CharacterInfo(**response_json)
    return character_info


def get_query_string_for_fields_list(fields: List[str]) -> str:
    if not fields:
        return ""

    field_str = "&fields="
    for field in fields:
        field_str += f"{field}%2C"

    return field_str
