import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'https://store.benjaminhardman.com/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        lst_img = []
        for cart in response.css('a.grid-product__link'):
            dict_img = {"src":cart.css('img').xpath('@src').get(),"title":cart.css('div.grid-product__title::text').get(),"price":cart.css('span.grid-product__price--original::text').get()}
            lst_img.append(dict_img)

    