import unittest
from unittest.mock import ANY, MagicMock, patch

import doob_bot.handler as db
from doob_bot.exceptions import BadStatusCode


class CharAPIRequestTests(unittest.TestCase):
    def setUp(self):
        self.em = MagicMock()
        self.prefix = "#info"
        self.two_args = ["name", "realm"]
        self.three_args = ["name", "realm", "Country"]

    def test_args_001(self):
        with self.assertRaises(ValueError):
            db.char_api_request([], self.prefix, self.em)

    @patch("doob_bot.handler.get_character_info")
    def test_args_002(self, mock):
        db.char_api_request(self.two_args, self.prefix, self.em)
        mock.assert_called_with("name", "realm", "#info")

    @patch("doob_bot.handler.get_character_info")
    def test_args_003(self, mock):
        db.char_api_request(self.three_args, self.prefix, self.em)
        mock.assert_called_with("name", "realm", "#info", "Country")


class GetCharInfoTests(unittest.TestCase):
    response_400 = MagicMock(status_code=400)
    response_200 = MagicMock(status_code=200, content="{}")

    @patch("requests.get", return_value=response_400)
    def test_response_001(self, mock):
        with self.assertRaises(BadStatusCode):
            db.get_character_info("name", "realm", "#info", "Region")

    @patch("requests.get", return_value=response_200)
    def test_response_002(self, mock):
        self.assertEqual({}, db.get_character_info("name", "realm", "#info", "Region"))

    @patch("requests.get", return_value=response_400)
    def test_bad_prefix_001(self, mock):
        with self.assertRaises(ValueError):
            db.get_character_info("name", "realm", "#random", "Region")


class HandleMessageTests(unittest.TestCase):
    def setUp(self):
        self.char_pref = MagicMock(content="#info name realm_name")
        self.mythic_pref = MagicMock(content="#foo bar baz")
        self.invalid_pref = MagicMock(content="#random foo bar")

    def test_invalid_pref_001(self):
        self.assertEqual(None, db.handle_message(self.invalid_pref))

    @patch("doob_bot.handler.char_api_request")
    @patch("discord.Embed", return_value=MagicMock())
    def test_char_pref_001(self, mock, api):
        db.handle_message(self.char_pref)
        api.assert_called_with(["name", "realm-name"], "#info", ANY)

    def test_mythic_pref_001(self):
        db.handle_message(self.mythic_pref)
