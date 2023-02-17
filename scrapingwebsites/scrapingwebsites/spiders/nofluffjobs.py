import scrapy


from scrapy.loader import ItemLoader
from scrapy.crawler import CrawlerProcess
from datetime import datetime

DATE = str(datetime.now())[:10]


class JobwebSpider(scrapy.Spider):
    name = 'jobweb'
    allowed_domains = ['nofluffjobs.com']
    start_urls = ['https://nofluffjobs.com/pl/python?page=1']

    def parse(self, response):
        name_of_the_page = 'https://nofluffjobs.com'
        for item in response.css('a.posting-list-item'):
            if item.css('span.text-uppercase.new-label.flex-shrink-0.ng-star-inserted::text').get() is not None:
                yield {
                    'job title': item.css('h3.posting-title__position::text').get(),
                    'company_name': item.css('span.posting-title__company::text').get(),
                    'link': f"{name_of_the_page}{item.css('a.posting-list-item::attr(href)').get()}",
                    'date': f"{DATE}",
                    'is_new': item.css('span.text-uppercase.new-label.flex-shrink-0.ng-star-inserted::text').get().strip()
                }
            else:
                yield {
                    'job title': item.css('h3.posting-title__position::text').get (),
                    'company_name': item.css('span.posting-title__company::text').get (),
                    'link': f"{name_of_the_page}{item.css ('a.posting-list-item::attr(href)').get ()}",
                    'date': f"{DATE}"
                }

        next_page = f"{name_of_the_page}{response.css('a[aria-label=Next]::attr(href)').get()}"
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)


# process = CrawlerProcess(settings={
#     "FEEDS": {
#         f"nofluffjons_{DATE}.json": {"format": "json"},
#     },
# })
#
