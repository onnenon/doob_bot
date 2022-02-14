import json
from typing import Any, Dict, List, Optional

import requests

from doob_bot.models import (
    BestRunData,
    CharacterInfoData,
    CommandCharacterData,
    HighestRunData,
    IoscoreData,
)
from doob_bot.settings import LOGGER

API_URL_BASE = "https://raider.io/api/v1/"
HEADERS = {"Content-Type": "application/json"}


def get_character_profile_info(
    char_data: CommandCharacterData,
    fields: Optional[List[str]],
) -> Dict[str, Any]:
    field_str = get_query_string_for_fields_list(fields)
    url = f"{API_URL_BASE}characters/profile?region={char_data.region}&realm={char_data.realm}&name={char_data.char_name}{field_str}"  # noqa: E501

    LOGGER.debug(url)

    response = requests.get(url, headers=HEADERS)
    response_json = json.loads(response.text)
    LOGGER.debug(response_json)
    return response_json


def get_query_string_for_fields_list(fields: List[str]) -> str:
    if not fields:
        return ""

    field_str = "&fields="
    for field in fields:
        field_str += f"{field}%2C"

    return field_str


def get_character_info_data(char_data: CommandCharacterData) -> CharacterInfoData:
    response_json = get_character_profile_info(char_data, ["gear", "guild"])

    character_info = CharacterInfoData(**response_json)
    return character_info


def get_ioscore_data(char_data: CommandCharacterData) -> IoscoreData:
    response_json = get_character_profile_info(char_data, ["mythic_plus_scores"])

    return IoscoreData(**response_json)


def get_highest_run_data(char_data: CommandCharacterData) -> HighestRunData:
    response_json = get_character_profile_info(
        char_data, ["mythic_plus_highest_level_runs"]
    )

    return HighestRunData(**response_json)


def get_best_run_data(char_data: CommandCharacterData) -> BestRunData:
    response_json = get_character_profile_info(char_data, ["mythic_plus_best_runs"])

    return BestRunData(**response_json)
