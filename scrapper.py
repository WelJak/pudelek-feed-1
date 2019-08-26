from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import csv

url = 'https://www.pudelek.pl'
client = uReq(url)
page_html = client.read()
client.close()
page_soup = soup(page_html, "html.parser")
entries = page_soup.findAll("div", {"class":"entry"})

filename = "entries.csv"
f = open(filename, "w")

headers = 'id; add_time; title; description; tags \n'

f.write(headers)

for entry in entries:
    tag = ''
    entry_id = entry["data-id"]
    time = entry.span.text
    title = entry.a.text.strip()
    desc = entry.p.text
    a = entry.find("span", {"class":"inline-tags"})
    children = a.findChildren("a", recursive=False)
    for i in range(len(children)):
        tag = tag + '/' + children[i].text.strip()
    f.write(entry_id + "; " + time + "; " + title + "; " + desc + "; " + tag + "\n")

f.close()

