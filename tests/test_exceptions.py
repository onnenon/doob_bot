import unittest

from doob_bot.exceptions import BadStatusCode


class ExeptionTests(unittest.TestCase):
    def test_status_code_001(self):
        self.assertEqual(400, BadStatusCode("").status_code)

    def test_status_code_002(self):
        self.assertEqual(200, BadStatusCode("", status_code=200).status_code)
