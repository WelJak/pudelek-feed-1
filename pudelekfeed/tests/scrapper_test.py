import unittest

from pudelekfeed.scrapper.scrapper import *

WEBSITE_URL = 'https://www.pudelek.pl'


class ScrapperTest(unittest.TestCase):
    def setUp(self):
        self.scrapper = Scrapper(WEBSITE_URL)
        self.news = self.scrapper.fetch_news_from_website()

    def test_check_instance(self):
        self.assertIsNotNone(self.news)
        self.assertIsInstance(self.news, list)
