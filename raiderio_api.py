"""
Raider.io API info at https://raider.io/api#!/
"""

import html
import json
import requests

API_URL_BASE = "https://raider.io/api/v1/"
HEADERS = {'Content-Type': 'application/json'}


def get_character(name: str, realm: str, prefix, region: str="US"):
    """ Return Character Info from Raider.io """
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
            field_str += "{}%2C".format(field)

    if field_str.endswith("0"):
        field_str = field_str[:-3]

    api_url = "{}characters/profile?region={}&realm={}&name={}{}".format(
        API_URL_BASE, region, realm, name, field_str)

    # print(api_url)

    response = requests.get(api_url, headers=HEADERS)

    if response.status_code == 200:
        # print(json.loads(response.content.decode('utf-8')))
        return json.loads(response.content.decode('utf-8'))
    return None
