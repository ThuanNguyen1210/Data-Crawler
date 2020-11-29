import requests
from bs4 import BeautifulSoup
import json

def trade_spider(max_page):
    count_company=0
    page = 1
    jobs_array = {}
    jobs = []
    while page <= max_page :
        url = "https://1001vieclam.com/search-results-jobs/?searchId=1606497144.676&action=search&"+str(page)+"&view=list"
        source = requests.get(url)
        soup = BeautifulSoup(source.text, "html.parser")
        for links in soup.findAll('div', {'class' : 'listing-title'}):
            sub_url = process(str(links))
            jobs.append(get_item(sub_url))
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
    info = soup.findAll('div', {'class', 'displayFieldBlock'})
    job_item = {}
    job_item["Tiêu đề"] = title_process(str(soup.find('div' , {'class' : 'listingInfo'})))
    

    for i in info:
        data_array = data_process(str(i))
        for i in range(len(data_array)):
            job_item[data_array[0]] = data_array[1]

    return job_item

def title_process(str_title):
    begin = str_title.find("<h1>") +4
    end = str_title.find("</h1>"  )
    return str_title[begin:end]

def data_process(data):
    category = ""
    value = ""
    xx= data.find("<ul><li>")
    
    yy= data.find("<!-- <pre>")
    aa= data.find("<!-- <h3>Tỉnh / Thành:</h3> -->")
    date = data.find("<!-- <h3>Ngày đăng:</h3> -->")
    if aa!=-1:
        begin = data.find("<h3>")+4
        middle = data.find("</h3>")
        end = data.find("</div>")
        category=data[begin+len("Tỉnh / Thành:</h3> --><h3>")+1:middle+len("Tỉnh / Thành:</h3> --><h3>")+1]
        value=data[middle+len("Tỉnh / Thành:</h3> --><h3>")+51:end-15]
        return[category,value]

    if yy!=-1:
        begin = data.find("<h3>")+4
        middle = data.find("</h3>")
        end = yy
        category=data[begin:middle]
        value = data[middle+97:end-61]
        return[category,value]
    
    
    if date!=-1:
        begin = data.find("<h3>")+4
        middle = data.find("</h3>")
        #datex= data.find("<div class="displayField">")
        end =data.find("</div>\n</div>")-10
        category=data[middle+14:middle+28]
        value = data[end:end+10]
        return[category,value]
   




    
    if xx==-1:
        begin = data.find("<h3>")+4
        middle = data.find("</h3>")
        end = data.find("</div>")
        category=data[begin:middle]
        value=data[middle+32:end]
        return[category,value]
    return[category,value]
        
    
  
  

    

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

def process(data):
    begin = data.find("href=\"")
    end = data.rfind("\">")
    return data[begin+len("href=\""):end]
trade_spider(50)
