from spylogger import get_logger

LOGGER = get_logger(log_level="DEBUG")

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
