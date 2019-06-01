from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen
import pprint

my_url = 'https://www.madesafe.org/science/hazard-list/#Exceptions'
req = Request(my_url, headers = {'User-Agent': 'Mozilla/5.0'})

web_byte = urlopen(req).read()
page_html = web_byte.decode('utf-8')


# html parsing
page_soup = soup(page_html, 'lxml')

# Grabs all headers
list_of_headers = []
for headings in page_soup.find_all('h3'):
    list_of_headers.append(headings.text.strip())

# Make a dictionary containment with keys as the headers in the above list and items as the div beneath those headers
containment = {}
i = 0
for j in range(1,4):
    for divs in page_soup.find_all("div", {"id": "accordion-" + str(j)}):
        div = divs.descendants
        for a_div in div:
            if a_div.name == 'div':
                containment[list_of_headers[i]] = a_div.get_text(strip=True)
                i = i + 1

pprint.pprint(containment)