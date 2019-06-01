# User selects a product and the link goes here
from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen


my_url = 'https://www.goodguide.com/products/420447-garnier-color-shield-shampoo-reviews-ratings#/'

def page_soup(my_url):
    req = Request(my_url, headers={'User-Agent': 'Mozilla/5.0'})

    web_byte = urlopen(req).read()
    page_html = web_byte.decode('utf-8')

    # html parsing
    return soup(page_html, 'lxml')

page_soup = page_soup(my_url)

# get rating
for thing in page_soup.find_all("p", {"class":"ring-value number"}):
    print(thing.text)
    break

# get ingredients
ingredients = []
for lists in page_soup.find_all("ul", {"class":"list product-details-ingredients"}):
    for a in lists.find_all('a'):
        ingredients.append(a.text)

# get links
links = []
for lists in page_soup.find_all("ul", {"class":"list product-details-ingredients"}):
    for a in lists.find_all('a'):
        link = a.get('href')
        links.append(link)

url = 'https://www.goodguide.com'
complete_links = []
for link in links:
    complete_links.append(url + link)
