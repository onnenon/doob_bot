from dataclasses import dataclass
from enum import Enum
from typing import Any, Dict

from pydantic import BaseModel


class WowClass(Enum):
    DH = "Demon Hunter"
    DK = "Death Knight"
    DRUID = "Druid"
    HUNTER = "Hunter"
    MONK = "Monk"
    MAGE = "Mage"
    PALADIN = "Paladin"
    PRIEST = "Priest"
    ROGUE = "Rogue"
    SHAMAN = "Shaman"
    WARRIOR = "Warrior"
    WARLOCK = "Warlock"


class WowRegion(Enum):
    US = "us"
    EU = "eu"
    KR = "kr"
    TW = "tw"


class WowFaction(Enum):
    ALLIANCE = "alliance"
    HORDE = "horde"


@dataclass
class Guild:
    name: str
    realm: str


class CharacterInfo(BaseModel):
    name: str
    class_: WowClass
    active_spec_name: str
    region: WowRegion
    realm: str
    faction: WowFaction
    gear: Dict[str, Any]
    guild: Guild
    thumbnail_url: str
    profile_url: str

    class Config:
        fields = {"class_": "class"}


DATA_LISTS = {
    "#info": [
        "name",
        "class",
        "active_spec_name",
        "region",
        "realm",
        "faction",
        "gear",
        "guild",
        "profile_url",
        "thumbnail_url",
    ],
    "#ioscore": [
        "name",
        "realm",
        "class",
        "active_spec_name",
        "mythic_plus_scores",
        "thumbnail_url",
        "all",
        "dps",
        "healer",
        "tank",
    ],
    "#best": [
        "name",
        "class",
        "active_spec_name",
        "realm",
        "mythic_plus_best_runs",
        "mythic_plus_highest_level_runs",
        "dungeon",
        "mythic_level",
        "num_keystone_upgrades",
        "score",
        "thumbnail_url",
    ],
    "#highest": [
        "name",
        "class",
        "active_spec_name",
        "realm",
        "mythic_plus_best_runs",
        "mythic_plus_highest_level_runs",
        "dungeon",
        "mythic_level",
        "num_keystone_upgrades",
        "score",
        "thumbnail_url",
    ],
}


FIELD_DATA = {
    "#info": ["gear", "guild"],
    "#ioscore": ["mythic_plus_scores"],
    "#best": ["mythic_plus_best_runs"],
    "#highest": ["mythic_plus_highest_level_runs"],
}

CHAR_PREFIX = ["#info", "#ioscore", "#best", "#highest"]

MYTHIC_PLUS_PREFIX = ["#foo"]
