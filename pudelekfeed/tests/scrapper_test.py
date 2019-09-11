import unittest

from pudelekfeed.scrapper.scrapper import *

WEBSITE_URL = 'https://www.pudelek.pl'


class ScrapperTest(unittest.TestCase):
    def setUp(self):
        self.scrapper = Scrapper(WEBSITE_URL)
        self.news = self.scrapper.fetch_news_from_website()
        self.date = '21.09.2019 12:30'

    def test_fetch_news_from_website_should_not_return_None_value(self):
        self.assertIsNotNone(self.news)

    def test_fetch_news_from_website_should_return_list_of_news(self):
        self.assertIsInstance(self.news, list)

    def test_create_date_should_return_standardized_date(self):
        self.assertEqual(self.scrapper.create_date(self.date), '2019-09-21 12:30:00')


if __name__ == '__main__':
    unittest.main()
