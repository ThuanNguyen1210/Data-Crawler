This is the crawler to crawl data from vietnamwork.com.
Changes compared with the previous code:
- Modify loginAndCraw.py file to crawl links of jobs from the web and change the name of
the file to getJobLinks.py
- Add crawlData.py to crawl detail information of each job corresponding to each link   that we get from executing getJobLinks.py file

To run this crawler. Please do the following steps:
1. Go to folder datacrawler/datacrawler/spiders
2. First, type this command:
    py getJobLinks.py
   => The links of jobs will be saved in joblinks.txt
3. Next, to craw data of jobs and save the information to json file, please type:
    scrapy crawl vietnamwork -O jobdata.json

=> See the result in jobdata.json file


selenium: python file.py

scrapy: scrapy crawl name(vietnamwork) -O datafile(json, csv,...)

-O: ghi đè
-o: ghi nối tiếp