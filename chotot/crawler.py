import requests
from bs4 import BeautifulSoup
import json

def trade_spider(max_page):
    count_company=0
    page = 1
    jobs_array = {}
    jobs = []
    while page <= max_page :
        url = "https://www.chotot.com/toan-quoc/viec-lam?page=" + str(page)
        source = requests.get(url)
        soup = BeautifulSoup(source.text, "html.parser")
        for links in soup.findAll('li', {'class' : 'wrapperAdItem___2woJ1'}):
            item = links.find('a')
            jobs.append(get_item("https://www.chotot.com"+item.get('href')))
            count_company += 1
        page += 1
        if count_company==1000:
            break

    jobs_array["jobs"] = jobs
    writeJSONFile(jobs_array)
    printToConsole(jobs)

def get_item(item_url):
    source = requests.get(item_url)
    soup = BeautifulSoup(source.text, "html.parser")
    info = soup.findAll('div', {'class', 'media-body media-middle'})
    job_item = {}
    job_item["Tiêu đề"] = str(title_process(str(soup.find('h1' , {'class' : 'adTilte___3UqYW'}))))

    for i in info:
        data_array = data_process(str(i))
        for i in range(len(data_array)):
            job_item[data_array[0]] = data_array[1]

    return job_item

def title_process(str_title):
    begin = str_title.find("<!-- -->") + 8
    end = str_title.find("<\h1>") - 4
    return str_title[begin:end]

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
            print(key + ': ' + value)
        print("------------------")
        index += 1

trade_spider(50)
