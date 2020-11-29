import scrapy
import string

urls = [] # Links reach to the page containing information of jobs
file = open('joblinks.txt', 'r')
links = file.readlines()
for link in links:
    urls += [link]
class DataSpider(scrapy.Spider):
    name = 'vietnamwork'

    start_urls = urls

    def parse(self, response):
        yield {
            'job-title': response.css('div.job-header-info h1.job-title::text').get().strip(),
            'company': response.css('div.job-header-info div.row a::text').get().strip(),
            'expired_time': response.css('div.job-header-info div.row')[2].css('div.col-sm-12 span.expiry.gray-light::text').get().strip(),
            'benefits': list(filter(None,([response.css('div.benefits div.benefit-name::text')[i].get().strip() \
                            for i in range(len(response.css('div.benefits div.benefit-name::text').getall()))
                        ]))),
            'description': list(filter(None, ([response.css('div.description::text')[i].get().strip() \
                            for i in range(len(response.css('div.description::text').getall()))
                            ]))),
            'requirements': list(filter(None, ([response.css('div.requirements::text')[i].get().strip() \
                                for i in range(len(response.css('div.requirements::text').getall()))
                            ]))),
            'locations': list(filter(None, ([response.css('div.location div.location-name::text')[i].get().strip() \
                            for i in range(len(response.css('div.location div.location-name::text').getall()))
                            ])))
        }