from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen
import pprint

my_url = 'http://www.safecosmetics.org/get-the-facts/chem-of-concern/'
req = Request(my_url, headers = {'User-Agent': 'Mozilla/5.0'})

web_byte = urlopen(req).read()
page_html = web_byte.decode('utf-8')


# html parsing
page_soup = soup(page_html, 'lxml')

# Grab all headers
def headers():
    headers = []
    for header in page_soup.find_all('h2'):
        headers.append(header.text.strip())
    return headers

# Grab all the links of chemicals and put it into a 'links'

def links():
    links = []
    for href in page_soup.find_all('h2'):
        try:
            link = href.find('a')
            links.append(link.get('href'))
        except:
            continue
    return links

if __name__ == 'main':
    headers()
    links()







