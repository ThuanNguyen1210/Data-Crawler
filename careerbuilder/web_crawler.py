import requests
from bs4 import BeautifulSoup

def trade_spider(max_page):
    page=1
    while page<= max_page :
        url = "https://careerbuilder.vn/viec-lam/tat-ca-viec-lam-trang-"+str(page)+"-vi.html"
        source= requests.get(url)
        #plain_text = source.text
        soup= BeautifulSoup(source.text, "html.parser")
        for links in soup.findAll('a', {'class' : 'job_link'}):
            href = links.get('href')
            print(href)
            get_item(href)
            print()
        page +=1

def get_item(item_url):
    
    source= requests.get(item_url)
    #plain_text = source.text
    soup= BeautifulSoup(source.text, "html.parser")
    for item_name in soup.findAll('p', {'class' : 'title'}):
            name_company = item_name.string
            print(name_company)

trade_spider(1)