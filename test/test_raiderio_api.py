import unittest


class FirstTests(unittest.TestCase):
    def test_1(self):
        self.assertEqual('Name', 'Name')


if __name__ == '__main__':
    unittest.main()