import scrapy
import string

urls = [] # Links reach to the page containing information of jobs
file = open('joblinks.txt', 'r')
links = file.readlines()
for link in links:
    urls += [link]

salaryfile = open('salary.txt', 'r', encoding='utf-8')
salaries_info = salaryfile.readlines()
salaries = []
for salary in salaries_info:
    salaries += [salary]
i = 0
class DataSpider(scrapy.Spider):
    name = 'vietnamwork'

    start_urls = urls
    def parse(self, response):
        global i
        yield {
            'job-title': response.css('div.job-header-info h1.job-title::text').get().strip(),
            'company': response.css('div.job-header-info div.row a::text').get().strip(),
            'salary': salaries[i].strip(),
            'location': list(filter(None, ([response.css('div.location div.location-name::text')[i].get().strip('+-–*o"•·\\>■\n\r\t ') \
                            for i in range(len(response.css('div.location div.location-name::text').getall()))
                            ]))),
            'position': response.css('div.job-header-info h1.job-title::text').get().strip(),
            'job_description': list(filter(None, ([response.css('div.description::text')[i].get().strip('+-–*o"•·\\>■\n\r\t ') \
                            for i in range(len(response.css('div.description::text').getall()))
                            ]))),
            'job_requirement': list(filter(None, ([response.css('div.requirements::text')[i].get().strip('+-–*o"•·\\>■\n\r\t ') \
                                for i in range(len(response.css('div.requirements::text').getall()))
                            ]))),
            'benefit': list(filter(None,([response.css('div.benefits div.benefit-name::text')[i].get().strip('+-–*o"•·\\>■\n\r\t ') \
                            for i in range(len(response.css('div.benefits div.benefit-name::text').getall()))
                        ]))),
            'quantity': "1"
        }
        i += 1