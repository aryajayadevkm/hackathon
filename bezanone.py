from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen
from chemicals_of_concern import headers, links
import pprint

urls = chemicals_of_concern.links
headings = chemicals_of_concern.headers

def page(url):
    my_url = 'url'
    req = Request(my_url, headers={'User-Agent': 'Mozilla/5.0'})

    web_byte = urlopen(req).read()
    page_html = web_byte.decode('utf-8')

    # html parsing
    page_soup = soup(page_html, 'lxml')

    # get 'what to look on labels'
    chem_list_unst = []
    for paras in page_soup.find_all("blockquote"):
        para = paras.descendants
        for a_para in para:
            try:
                if a_para.text.strip() == "WHAT TO LOOK FOR ON THE LABEL":
                    chem_list_unst.append(a_para.next_element.next_element.strip(':'))
            except:
                continue

    # get hazards
    chemical =
    for item in chem_list_unst:
        if chemical in str(chem_list_unst):
            # print('yes! found it')
            for paras in page_soup.find_all("blockquote"):
                para = paras.descendants
                for a_para in para:
                    try:
                        if a_para.text.strip() == "HEALTH CONCERNS":
                            health_concerns.append(a_para.next_element.next_element.strip(':'))
                    except:
                        continue

if __name__ == "main":
    page(url)
