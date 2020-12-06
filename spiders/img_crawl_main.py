import scrapy
import os
import requests as rq

class QuotesSpider(scrapy.Spider):
    name = "quotes1"

    def start_requests(self):
        urls = [
            'https://benjaminhardman.com/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        lst_img = []
        i=0
        for cart in response.css('div.thumbnail'):
            dict_img = {"src":cart.css('img').xpath('@data-src').get(),"title":"image"+str(i)}
            i+=1
            lst_img.append(dict_img)
        
        print(lst_img)

        #write list image to folder
        os.mkdir('img_mainpage')

        for i in lst_img:
            title = i['title']
            img_data = rq.get(i['src']).content
            with open("img_mainpage/"+title+'.jpg','wb+') as f:
                f.write(img_data)
                f.close()