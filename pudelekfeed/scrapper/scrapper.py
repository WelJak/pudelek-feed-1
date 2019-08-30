import sys
import traceback

from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as Soup
from pudelekfeed import logger


class Scrapper:
    def __init__(self, url):
        self.url = url

    def fetch_messages_from_pudelek(self):
        try:
            client = ureq(self.url)
            page_html = client.read()
            client.close()
        except:
            logger.info('An error occurred during establishing connection with {}'.format(self.url))
            traceback.print_exc(file=sys.stdout)
            client.close()
        page_soup = Soup(page_html, "html.parser")
        entries = page_soup.findAll("div", {"class": "entry"})
        output = list(map(lambda part: self.create_output_part(part), entries))
        return output

    def create_output_part(self, entry):
        entry_id = entry["data-id"]
        time = entry.span.text
        title = entry.a.text.strip()
        desc = entry.p.text
        a = entry.find("span", {"class": "inline-tags"})
        children = a.findChildren("a", recursive=False)
        tags = list(map(lambda child: child.text.strip(), children))
        link = entry.find(lambda tag: tag.get('href'))['href']
        part = dict(id=entry_id, date=time, title=title, description=desc, tags=tags, link=link)
        return part
