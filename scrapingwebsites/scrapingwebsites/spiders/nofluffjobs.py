import scrapy


class JobwebSpider(scrapy.Spider):
    name = 'jobweb'
    allowed_domains = ['nofluffjobs.com']
    start_urls = ['https://nofluffjobs.com/pl/python?page=1']
    def parse(self, response):
        name_of_the_page = 'https://nofluffjobs.com'
        for item in response.css('a.posting-list-item'):
            yield {
                'job title': item.css('h3.posting-title__position::text').get(),
                'company_name': item.css('span.posting-title__company::text').get(),
                'link': f"{name_of_the_page}{item.css('a.posting-list-item::attr(href)').get()}"
            }
        next_page = f"{name_of_the_page}{response.css('a[aria-label=Next]::attr(href)').get()}"
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

#scrapy crawl jobweb -O webjobs.csv
