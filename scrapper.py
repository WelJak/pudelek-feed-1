from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import csv

url = 'https://www.pudelek.pl'
strona = uReq(url)
strona_html = strona.read()
strona.close()
strona_soup = soup(strona_html, "html.parser")
wpisy = strona_soup.findAll("div", {"class":"entry"})

filename = "wpisy.csv"
f = open(filename, "w")

naglowki = 'id, czas, tytul, opis \n'

f.write(naglowki)

for wpis in wpisy:
    wpis_id = wpis["data-id"]
    czas = wpis.span.text
    tytul = wpis.a.text.strip()
    opis = wpis.p.text
    # tagi ??
    f.write(wpis_id + ", " + czas + ", " + tytul + ", " + opis + "\n")
    #print(wpis_id)

f.close()

