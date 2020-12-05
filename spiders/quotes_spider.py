import scrapy
import os
import requests as rq

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

        #write list image to folder
        os.mkdir('store_img')

        for i in lst_img:
            title = i['title'].replace(' ','_')+'_'+i['price']
            img_data = rq.get('https:'+i['src']).content
            with open("store_img/"+title+'.jpg','wb+') as f:
                f.write(img_data)
                f.close()



    