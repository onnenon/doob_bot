import unittest
from unittest.mock import MagicMock, patch

import doob_bot.raiderio_api as db
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

    @patch("doob_bot.raiderio_api.get_character_info")
    def test_args_002(self, mock):
        db.char_api_request(self.two_args, self.prefix, self.em)
        mock.assert_called_with("name", "realm", "#info")

    @patch("doob_bot.raiderio_api.get_character_info")
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
        self.assertEqual({},
                         db.get_character_info("name", "realm", "#info",
                                               "Region"))

    @patch("requests.get", return_value=response_400)
    def test_bad_prefix_001(self, mock):
        with self.assertRaises(ValueError):
            db.get_character_info("name", "realm", "#random", "Region")
