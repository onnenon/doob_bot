"""
Raider.io API info at https://raider.io/api#!/
"""

import html
import json
import requests

API_URL_BASE = "https://raider.io/api/v1/"
HEADERS = {'Content-Type': 'application/json'}


def get_character(name: str, realm: str=None, region: str="US", fields: list=[]):
    """ Return Character Info from Raider.io """

    field_str = ""
    if len(fields) > 0:
        field_str += "&fields="
        for field in fields:
            field_str += "{}%2C%20".format(field)

    api_url = "{}characters/profile?region={}&realm={}&name={}{}".format(
        API_URL_BASE, region, realm, name, field_str)

    response = requests.get(api_url, headers=HEADERS)

    if response.status_code == 200:
        print(json.loads(response.content.decode('utf-8')))
        return json.loads(response.content.decode('utf-8'))
    return None
