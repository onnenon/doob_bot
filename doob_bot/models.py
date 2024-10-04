from enum import Enum
from typing import Any, Dict

from pydantic import BaseModel
from pydantic.dataclasses import dataclass


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


@dataclass
class CommandCharacterData:
    char_name: str
    realm: str
    region: str = "us"


class MythicPlusScores(BaseModel):
    all: str
    tank: str
    healer: str
    dps: str

    class Config:
        extra = "ignore"


class CharacterBaseData(BaseModel):
    name: str
    realm: str
    class_: WowClass
    active_spec_name: str
    thumbnail_url: str

    class Config:
        extra = "ignore"
        fields = {"class_": "class"}


class CharacterInfoData(CharacterBaseData):
    region: WowRegion
    faction: WowFaction
    gear: Dict[str, Any]
    guild: Guild
    profile_url: str


class IoscoreData(CharacterBaseData):
    mythic_plus_scores: MythicPlusScores


class HighestRunData(CharacterBaseData):
    pass


class BestRunData(CharacterBaseData):
    pass


DATA_LISTS = {
    "#ioscore": [
        "mythic_plus_scores",
        "all",
        "dps",
        "healer",
        "tank",
    ],
    "#best": [
        "mythic_plus_best_runs",
        "mythic_plus_highest_level_runs",
        "dungeon",
        "mythic_level",
        "num_keystone_upgrades",
        "score",
    ],
    "#highest": [
        "mythic_plus_best_runs",
        "mythic_plus_highest_level_runs",
        "dungeon",
        "mythic_level",
        "num_keystone_upgrades",
        "score",
    ],
}
