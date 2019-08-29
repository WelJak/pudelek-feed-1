from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq


class Scrapper:

    def fetch_list_of_entries(self):

        url = 'https://www.pudelek.pl'
        client = uReq(url)
        page_html = client.read()
        client.close()
        page_soup = soup(page_html, "html.parser")
        entries = page_soup.findAll("div", {"class": "entry"})

        output = []
        for entry in entries:
            tags = []
            entry_id = entry["data-id"]
            time = entry.span.text
            title = entry.a.text.strip()
            desc = entry.p.text
            a = entry.find("span", {"class": "inline-tags"})
            children = a.findChildren("a", recursive=False)
            for i in range(len(children)):
                tag = children[i].text.strip()
                tags.append(tag)
            for a in entry.find_all('a', href=True):
                links = a['href']
            part = dict(id=entry_id, date=time, title=title, description=desc, tags=tags, link=links)
            output.append(part)
        return output
