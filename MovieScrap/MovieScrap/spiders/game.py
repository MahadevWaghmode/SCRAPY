import scrapy


class QuotesSpider(scrapy.Spider):
    name = "games"
    start_urls = [
        'http://oceanofgames.com/',
    ]

    def parse(self, response):
        for quote in response.css('div.post-details'):
            yield {
                'name': quote.css('h2.title a::text').get(),
                'link' : quote.css('h2.title a::attr(href)').get(),
                'tags': quote.css('div.post-info a::text').getall(),
            }

        next_page = response.css('a.next::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)