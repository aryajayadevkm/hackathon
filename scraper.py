from urllib.request import urlopen
from bs4 import BeautifulSoup as soup



def title():
    print(
        "****************************************** ingredient********************************************\n\n")
    # searching
    d = "+".join(l)

    # searching
    my_url = "https://www.goodguide.com/products?utf8=%E2%9C%93&filter="+d+"&button=#/"
    print(my_url)

    # calling the fn
    uClient = urlopen(my_url)
    page_soup = soup(uClient.read(), "html.parser")
    uClient.close()
    name = page_soup.findAll("span", {"class": "auto-truncated"})
    #productDivs = soup.findAll('div', attrs={'class': 'large-6 columns'})
    #for div in productDivs:
        #link = div.find('a')
        #print(link.get('href'))
    try:
        for i in range(0, 8):
            print( i+1, ".", name[i].text),
            #print(href[i].text)
            print("\n_________________\n")
        print("enter the product you want to search")

    except:
        print("the product is not found ")
        i = 1

def details():
    my_url = "https://www.goodguide.com/products?utf8=%E2%9C%93&filter="+d+"&button=#/"
    print(my_url)
    # calling the fn
    uClient = urlopen(my_url)
    page_soup = soup(uClient.read(), "html.parser")
    uClient.close()
    name = page_soup.findAll("span", {"class": "auto-truncated"})

a=input("Enter product name  -  ")
i=0
l=a.split(" ")
title()
print("\n\n")
#if(i==0):
#    details()