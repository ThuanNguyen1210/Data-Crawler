import scrapy


class JobSpider(scrapy.Spider):
    name = 'mywork'

    start_urls = ['https://mywork.com.vn/tuyen-dung']

    def parse(self, response):
        links = response.css('div.content p.j_title a::attr("href")').getall()
        for link in links:
            link = 'https://mywork.com.vn' + link
            yield scrapy.Request(url=link, callback=self.parse_job_info)

    def parse_job_info(self, response):
        yield {
            'job_title': str(response.css('h1.main-title span::text').get()).strip(),
            'company': str(response.css('h4.desc-for-title span::text').get()).strip(),
            'salary': str(response.css('div.box_main_info_job_left  div.row')[0].css('div.col-md-6')[0].css('span::text')[1].get()).strip(),
            'expired_day': str(response.css('div.box_main_info_job_left  div.row')[0].css('div.col-md-6')[1].css('span::text')[1].get()).strip(),
            'location': str(response.css('div.box_main_info_job_left  div.row')[1].css('div.col-md-6')[0].css('span div.txt_ellipsis::text').get()).strip(),
            'major': str(response.css('div.box_main_info_job_left  div.row')[1].css('div.col-md-6')[1].css('span div.txt_ellipsis::text').get()).strip(),
            'position': str(response.css('div.box_main_info_job_left  div.row')[2].css('div.col-md-6')[0].css('span::text')[1].get()).strip(),
            'experience': str(response.css('div.box_main_info_job_left  div.row')[2].css('div.col-md-6')[1].css('span::text')[1].get()).strip(),
            'form_of_work': str(response.css('div.box_main_info_job_left  div.row')[3].css('div.col-md-6')[0].css('span::text')[1].get()).strip(),
            'degree_requirement': str(response.css('div.box_main_info_job_left  div.row')[3].css('div.col-md-6')[1].css('span::text')[1].get()).strip(),
            'quantity': str(response.css('div.box_main_info_job_left  div.row')[4].css('div.col-md-6')[0].css('span::text')[1].get()).strip(),
            'gender_requirement': str(response.css('div.box_main_info_job_left  div.row')[4].css('div.col-md-6')[1].css('span::text')[1].get()).strip(),
        }
