import unittest

from .inmemory_checker import *


class InMemoryCheckerTest(unittest.TestCase):
    def setUp(self):
        self.x = InMemoryChecker()
        self.x.entries = ['message']

    def test_check_response(self):
        self.assertFalse(self.x.check('message'))
        self.assertTrue(self.x.check('not sent message'))

    def test_marking_output(self):
        self.x.mark('marked_message')
        self.assertEqual(self.x.entries, ['message', 'marked_message'])


if __name__ == '__main__':
    unittest.main()
