from unittest import TestCase, skip
from doob_bot import on_message


class BotTest(TestCase):
    def test_001_on_message(self):
        hm = doob_bot.handler()

