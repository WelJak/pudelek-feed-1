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
            entries = page_soup.findAll("div", {"class": "entry"})
            output = list(map(lambda part: self.create_output_part(part), entries))
            return output
        except:
            logger.info('An error occurred during establishing connection with {}'.format(self.url))
            traceback.print_exc(file=sys.stdout)

    @staticmethod
    def create_date(time):
        months = time.split('.')
        year = months[2].split(' ')
        hours_and_minutes = year[1].split(':')
        date = months[:2] + hours_and_minutes[::]
        date.insert(0, year[0])
        date.append('0')
        date = list(map(lambda x: int(x), date))
        return str(datetime.datetime(date[0], date[2], date[1], date[3], date[4], date[5]))

    def create_output_part(self, entry):
        entry_id = entry["data-id"]
        time = self.create_date(entry.span.text)
        title = entry.a.text.strip()
        desc = entry.p.text
        a = entry.find("span", {"class": "inline-tags"})
        children = a.findChildren("a", recursive=False)
        tags = list(map(lambda child: child.text.strip(), children))
        link = entry.find(lambda tag: tag.get('href'))['href']
        part = dict(id=entry_id, date=time, title=title, description=desc, tags=tags, link=link)
        return part
