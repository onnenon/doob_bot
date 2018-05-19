import html
import json
import requests

API_URL_BASE = "https://raider.io/api/v1/"
HEADERS = {'Content-Type': 'application/json'}


def get_character(name: str, realm="Shattered Hand", region="US"):
    """
    Return Character Info from Raider.io

    Return Data Structure
    {
        'name': 'Doobleykah',
        'race': 'Night Elf',
        'class': 'Druid',
        'active_spec_name': 'Restoration',
        'active_spec_role': 'HEALING',
        'gender': 'male',
        'faction': 'alliance',
        'achievement_points': 8190,
        'honorable_kills': 1859,
        'thumbnail_url': 'https://render-us.worldofwarcraft.com/character/shattered-hand/225/135521505-avatar.jpg?alt=wow/static/images/2d/avatar/4-0.jpg',
        'region': 'us',
        'realm': 'Shattered Hand',
        'profile_url': 'https://raider.io/characters/us/shattered-hand/Doobleykah'
    }

    """
    realm = html.escape(realm)

    api_url = "{}characters/profile?region={}&realm={}&name={}".format(
        API_URL_BASE, region, realm, name)

    response = requests.get(api_url, headers=HEADERS)

    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None
