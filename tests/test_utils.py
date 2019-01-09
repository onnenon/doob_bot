import unittest

from discord import Embed
import doob_bot.utils as db


class UtilsTests(unittest.TestCase):
    def setUp(self):
        self.em = Embed()
        self.li = ["key_1", "key_2", "key_3"]
        self.data = {"thumbnail_url": "https://localhost"}
        self.value_is_dict = {"key_1": {"key_2": "value"}}
        self.value_is_list = {
            "key_1": [{
                "key_2": "value_2"
            }, {
                "key_3": "value3"
            }, {
                "random": "random_value"
            }]
        }
        self.value_is_string = {"key_1": "value_1"}

    def test_add_thumbnail_001(self):
        embed = db.add_data_to_embed(self.em, self.li, **self.data)
        self.assertEqual("https://localhost", embed.thumbnail.url)

    def test_iteration_dict_value(self):
        embed = db.add_data_to_embed(self.em, self.li, **self.value_is_dict)
        self.assertEqual("Key 2: value\n", embed.fields[0].value)
        self.assertEqual(embed.fields[0].name, "Key 1")

    def test_iteration_list_value(self):
        embed = db.add_data_to_embed(self.em, self.li, **self.value_is_list)
        self.assertEqual("Key 2: value_2\n", embed.fields[0].value)
        self.assertEqual("Key 3: value3\n", embed.fields[1].value)

    def test_iteration_str_value(self):
        embed = db.add_data_to_embed(self.em, self.li, **self.value_is_string)
        self.assertEqual("Key 1:", embed.fields[0].name)
        self.assertEqual("value_1", embed.fields[0].value)