import json
import requests
from bs4 import BeautifulSoup

def trade_spider(max_page):
    data = {}
    jobs=[]
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
            ##print(href)
            jobs.append(get_item(href,count_company))
            print("craw item",count_company)
            #test 5 company
            if count_company==1000:
                break
        page +=1
        if count_company==1000:
            break
    data['jobs']=jobs
    #print(count_company)
    write_file(data)

def get_item(item_url,id):
    jobs_item={}
    source= requests.get(item_url)
    soup= BeautifulSoup(source.text, "html.parser")

    jobs_item['ID']=str(id)
    item = soup.find('a', {'class' : 'employer job-company-name'})
    if item:
        name_company = item.string
        link_company= item.get('href')
        jobs_item['Tên công ty']=name_company
        #print(name_company)
        #print(link_company)
        location=info_company(link_company)
        jobs_item['Địa điểm']=location
    else:
        jobs_item['Tên công ty']=""

    item = soup.find('p', {'class' : 'title'})
    if item:
        job = item.string
        #print(job)
        jobs_item['Vị trí tuyển dụng']=job
    else:
        jobs_item['Vị trí tuyển dụng']=""
    
    #print("info jobs")
    for item in soup.findAll('div', {'class' : 'detail-box has-background'}):
        for subitem in item.findAll('li'):
            jobs_item[subitem.find('strong').text.strip()]=subitem.find('p').text.strip()
            #print(subitem.find('strong').text.strip()," : ",subitem.find('p').text.strip())

    
    tempstring=""
    for item in soup.findAll('ul', {'class' : 'welfare-list'}):
        for subitem in item.findAll('li'):
            tempstring = tempstring + subitem.text+ ", "
        tempstring = tempstring[:-2]
    jobs_item['Phúc lợi']=tempstring   
    #print("Phúc lợi: ", tempstring)

    for item in soup.findAll('div', {'class' : 'detail-row'}):
        arr=item.text.split('\n')
        temparr=[]
        for i in arr[2:]:
            ##print(i)
            if i!="":
                temparr = temparr + [i]
        jobs_item[arr[1].strip()]=temparr
        #print(item.text.split('\n')[2:])

    return jobs_item

def info_company(item_url):
    source= requests.get(item_url)
    if source:
        soup= BeautifulSoup(source.text, "html.parser")

        item = soup.find('div', {'class' : 'company-info'})
        if item:
            subitem = item.find('div', {'class' : 'content'})
            if subitem:
                location = subitem.text
                #print(location.split('\n')[3])
                return location.split('\n')[3]
            
    return ""

def write_file(data):
    json_object = json.dumps(data, indent=len(data.keys()))
    with open('data.json', 'w', encoding='utf-8') as outfile:
        outfile.write(json_object)
trade_spider(30)
 
    #json.dump(data, outfile, ensure_ascii=False)
#with open('data.txt', 'w', encoding='utf-8') as outfile:
    #json.dump(data, outfile, ensure_ascii=False)
