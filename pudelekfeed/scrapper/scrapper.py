import datetime
import sys
import traceback
from urllib.request import urlopen as ureq

from bs4 import BeautifulSoup as Soup

import logger


class Scrapper:
    def __init__(self, url):
        self.url = url

    def fetch_news_from_website(self):
        try:
            client = ureq(self.url)
            page_html = client.read()
            client.close()
            page_soup = Soup(page_html, "html.parser")
            entries = page_soup.findAll("div", {"class": "sc-1gawtz3-0 hvcEVd"})[1:]
            output = list(map(lambda part: self.create_output_part(part), entries))
            return output
        except:
            logger.info('An error occurred during establishing connection with {}'.format(self.url))
            traceback.print_exc(file=sys.stdout)

    def create_output_part(self, entry):
        link = self.url + entry.find("a", {"class": "kbtsi-0 dxRpaj"}).get('href')
        entry_id = link[-17:]
        title = entry.a.text.strip()
        desc = entry.find("span", {"class": "sc-1x16xpf-1 bToylQ"}).text.strip()
        time = self.create_date(entry.find("span", {"class": "thnna0-0 hweFyO"}).text.strip())
        tags = self.get_tags(link)
        part = dict(id=entry_id, date=time, title=title, description=desc, tags=tags, link=link)
        return part

    @staticmethod
    def create_date(time):
        if 'min' in time:
            return (datetime.datetime.now() - datetime.timedelta(minutes=int(time[:2]))).strftime('%d.%m.%Y %H:%M')
        if 'godz' in time:
            return (datetime.datetime.now() - datetime.timedelta(hours=int(time[:2]))).strftime('%d.%m.%Y %H:%M')

    @staticmethod
    def get_tags(link):
        client = ureq(link)
        page_html = client.read()
        client.close()
        page_soup = Soup(page_html, "html.parser")
        return list(map(lambda tag: tag.text.strip(),
                        page_soup.findAll("div", {"class": "sc-7hqr3i-0 am69kv-0 sc-1pabckk-0 cOjdJX"})))


x = Scrapper('https://www.pudelek.pl')
print(x.fetch_news_from_website())
