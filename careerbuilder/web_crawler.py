import json
import requests
from bs4 import BeautifulSoup

def trade_spider(max_page):
    data = {}
    jobs=[]
    count_company=0
    page=1
    while page<= max_page :
        print()
        print("Page: ", page)
        print()
        url = "https://careerbuilder.vn/viec-lam/tat-ca-viec-lam-trang-"+str(page)+"-vi.html"
        source= requests.get(url)
        #plain_text = source.text
        soup= BeautifulSoup(source.text, "html.parser")
        for links in soup.findAll('a', {'class' : 'job_link'}):
            count_company += 1
            href = links.get('href')
            title=links.get('title')
            ##print(href)
            tempjob={}
            tempjob=get_item(href,title)
            if tempjob != {}:
                jobs.append(tempjob)
            else:
                count_company-=1
            print(count_company, ": ",title)
            #test 5 company
            
            if count_company==2000:
                break
        if count_company==2000:
            print("End ", page)
            break
            
        page +=1
    data['jobs']=jobs
    #print(count_company)
    write_file(jobs)
def checkdata(tempjob):
    for i in tempjob:
        if tempjob[i]=="" and i!="quantity":
            return False
    return True
def get_item(item_url,title):
    jobs_item={}
    source= requests.get(item_url)
    soup= BeautifulSoup(source.text, "html.parser")
    #print(title)
    jobs_item['job_title']=title
    
    # item = soup.find('p', {'class' : 'title'})
    # if item:
    #     job = item.string
    #     #print(job)
    #     jobs_item['Vị trí tuyển dụng']=job
    # else:
    #     jobs_item['Vị trí tuyển dụng']=""
    location=""
    item = soup.find('a', {'class' : 'employer job-company-name'})
    if item:
        name_company = item.string
        link_company= item.get('href')
        jobs_item['company']=name_company
        #print(name_company)
        #print(link_company)
        location=info_company(link_company)
        
    else:
        jobs_item['company']=""
        return {}



    #print("info jobs")
    salary=""
    jobtype=""
    requi=""
    for item in soup.findAll('div', {'class' : 'detail-box has-background'}):
        for subitem in item.findAll('li'):
            temp=subitem.find('strong').text.strip()
            if temp=="Lương":
                salary=subitem.find('p').text.strip()
            elif temp=="Ngành nghề":
                jobtype=subitem.find('p').text.strip()
            elif temp=="Kinh nghiệm":
                requi=subitem.find('p').text.strip()
            #jobs_item[subitem.find('strong').text.strip()]=subitem.find('p').text.strip()
            #print(subitem.find('strong').text.strip()," : ",subitem.find('p').text.strip())
    if salary=="" or location=="" or title== "" or requi=="":
        return {}
    jobs_item['salary']=salary
    jobs_item['location']=location
    jobs_item['position']=title

    # stringtype=""
    # typearr=jobtype.split('\n')
    # tempcount=0
    # iint=-1
    # for istring in typearr:
    #     iint+=1
    #     if iint==tempcount:
    #         #print(istring.strip())
    #         stringtype+=istring.strip()+", "
    #         tempcount +=3
    # stringtype=stringtype[:-2]  
    # jobs_item['job_type']=stringtype
    

    

    for item in soup.findAll('div', {'class' : 'detail-row'}):
        arr=item.text.split('\n')
        temparr=""
        for i in arr[2:]:
            ##print(i)
            if i!="":
                temparr = temparr + i
        if arr[1].strip()=="Mô tả Công việc":
            jobs_item['job_description']=temparr
            break
        #print(item.text.split('\n')[2:])

    jobs_item['job_requirement']=requi

    tempstring=""
    for item in soup.findAll('ul', {'class' : 'welfare-list'}):
        for subitem in item.findAll('li'):
            tempstring = tempstring + subitem.text+ ", "
        tempstring = tempstring[:-2]
    
    jobs_item['benefit']=str(tempstring)
    #print("Phúc lợi: ", tempstring)
    jobs_item['quantity']=""
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
    #json_object = json.dumps(data, indent=len(data.keys()),ensure_ascii=False)
    with open('data_p1.json', 'w', encoding='utf-8') as outfile:
        json.dump(data, outfile, ensure_ascii=False)
trade_spider(100)

    #json.dump(data, outfile, ensure_ascii=False)
#with open('data.txt', 'w', encoding='utf-8') as outfile:
    #json.dump(data, outfile, ensure_ascii=False)
