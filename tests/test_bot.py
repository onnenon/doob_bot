from unittest import TestCase, skip
from doob_bot import on_message


class BotTest(TestCase):
    @skip
    def test_001_invalid_arguments(self):
        with self.assertRaises(ValueError):
            pass
