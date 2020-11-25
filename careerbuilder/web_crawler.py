import json
import requests
from bs4 import BeautifulSoup

def trade_spider(max_page):
    data['info_company']=[]
    count_company=0
    page=1
    while page<= max_page :
        url = "https://careerbuilder.vn/viec-lam/tat-ca-viec-lam-trang-"+str(page)+"-vi.html"
        source= requests.get(url)
        #plain_text = source.text
        soup= BeautifulSoup(source.text, "html.parser")
        for links in soup.findAll('a', {'class' : 'job_link'}):
            count_company += 1
            href = links.get('href')
            print(href)
            get_item(href)
            print()
            #test 5 company
            if count_company==5:
                break
        page +=1

    print(count_company)

def get_item(item_url):
    
    source= requests.get(item_url)
    soup= BeautifulSoup(source.text, "html.parser")

    item = soup.find('p', {'class' : 'title'})
    job = item.string
    print(job)

    item = soup.find('a', {'class' : 'employer job-company-name'})
    name_company = item.string
    link_company= item.get('href')
    data['info_company'].append({
        'Tên công ty': name_company
    })
    print(name_company)
    print(link_company)

    for item in  soup.findAll('div', {'class' : 'map'}):     
        for subitem in  item.findAll('strong'):  
            title1= subitem.text
            print(title1)
def info_company(item_url):
    source= requests.get(item_url)
    soup= BeautifulSoup(source.text, "html.parser")
    for item in soup.findAll('p', {'class' : 'title'}):
            job = item.string
            print(job)
data = {}
trade_spider(1)
with open('data.txt', 'w', encoding='utf-8') as outfile:
    json.dump(data, outfile, ensure_ascii=False)
