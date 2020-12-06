import requests
from bs4 import BeautifulSoup
import json

def trade_spider(max_page):
    count_company=0
    page = 1
    jobs_array = {}
    jobs = []
    while page <= 200:
        url = "https://www.chotot.com/toan-quoc/viec-lam?page=" + str(page)
        source = requests.get(url)
        soup = BeautifulSoup(source.text, "html.parser")
        for links in soup.findAll('li', {'class' : 'wrapperAdItem___2woJ1'}):
            item = links.find('a')
            jobs.append(get_item("https://www.chotot.com"+item.get('href')))
            count_company += 1
        page += 1
        if count_company == 5000:
            break

    jobs_array["jobs"] = jobs
    writeJSONFile(jobs_array)
    printToConsole(jobs)

def get_item(item_url):
    source = requests.get(item_url)
    soup = BeautifulSoup(source.text, "html.parser")
    info = soup.findAll('div', {'class', 'media-body media-middle'})
    #Temporary store data crawled
    temp = {}
    temp["Tiêu đề"] = title_process(str(soup.find('h1' , {'class' : 'adTilte___3UqYW'})))
    temp["Lương"] = salary_process(str(soup.find('span', {'itemprop' : 'price'})))
    temp["Mô tả"] = description_process(str(soup.findAll('div', {'class' : 'd-lg-none d-block col-xs-12 no-padding'})[2]))

    for i in info:
        data_array = data_process(str(i))
        for i in range(len(data_array)):
            temp[data_array[0]] = data_array[1]

    #Filter data need to store
    job_item = filter_data(temp)
    print(job_item)
    return job_item

def title_process(title):
    begin = title.find("<!-- -->") + 8
    end = title.find("<\h1>") - 4
    return title[begin:end]

def salary_process(salary):
    begin = salary.find("<span itemprop=\"price\">") + len("<span itemprop=\"price\">")
    end = salary.find("<!-- -->")
    return salary[begin:end]

def description_process(description):
    begin = description.find('<p style=\"white-space:pre-line\">') + len('<p style=\"white-space:pre-line\">')
    end = description.find('</p>')
    para = description[begin:end]
    list_description = []

    while(para.find("\n") != -1):
        temp = para.find("\n")
        list_description.append("-" + para[0:temp])
        para = para[temp + 1:]

    return list_description

def data_process(data):
    category = ""
    value = ""
    begin = data.find("<span><span>")
    if begin != -1:
        middle = data.find("</span><span class=\"adParamValue___2xfwb\">")
        end = data.find("</span></span>")
        category = data[begin + len("<span><span>"):middle - 2]
        value = data[middle + len("</span><span class=\"adParamValue___2xfwb\">"):end]
    else:
        begin = data.find("<span class=\"fz13\">")
        end = data.find("</span>")
        category = "Địa chỉ"
        value = data[begin + len("<span class=\"fz13\">"):end]

    return [category, value]

def filter_data(dict):
    job = {}
    if "Tiêu đề" in dict:
        job['Title'] = dict["Tiêu đề"]
    if "Tên công ty" in dict:
        job['Company'] = dict['Tên công ty']
    if "Lương" in dict:
        job['Salary'] = dict['Lương']
    if "Địa chỉ" in dict:
        job['Location'] = dict['Địa chỉ']
    if "Loại công việc" in dict:
        job['Type'] = dict['Loại công việc']
    if "Ngành nghề" in dict:
        job['Position'] = dict['Ngành nghề']
    if "Mô tả" in dict:
        job['Description'] = dict['Mô tả']
    if "Chứng chỉ / kỹ năng" in dict:
        job['Requirement'] = dict['Chứng chỉ / kỹ năng']
    if "Các quyền lợi khác" in dict:
        job['Benefit'] = dict['Các quyền lợi khác']
    if "Số lượng tuyển dụng" in dict:
        job['Quantity'] = dict["Số lượng tuyển dụng"]
    return job 

def writeJSONFile(dictionary):
    # Serializing json  
    json_object = json.dumps(dictionary, indent=len(dictionary.keys()), ensure_ascii=False)

    # Writing to sample.json 
    with open("sample.json", "a", encoding='utf8') as outfile: 
        outfile.write(json_object) 

def printToConsole(dictionary):
    index = 1
    for i in dictionary:
        print(index)
        for key, value in i.items():
            print(key + ': ')
            print(value)
        print("------------------")
        index += 1

trade_spider(50)
