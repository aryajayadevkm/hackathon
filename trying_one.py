# get info of one ingredient
from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen
import pprint

my_url = 'https://www.goodguide.com/ingredients/479494-amyl-cinnamal-ingredient-information-reviews?category_id=152758&product_id=420447#/'
req = Request(my_url, headers={'User-Agent': 'Mozilla/5.0'})

web_byte = urlopen(req).read()
page_html = web_byte.decode('utf-8')

# html parsing
page_soup = soup(page_html, 'lxml')

# to get description
for item in page_soup.find_all("div", {"class": "large-offset-3 large-6 columns"}):
    ul = item.descendants
    for thing in ul:
        try:
            for li in thing.find_all("li"):
                print(li.text)
        except:
            continue


