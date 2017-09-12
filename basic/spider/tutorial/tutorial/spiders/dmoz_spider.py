#-*-coding:UTF-8-*-
import scrapy
from tutorial.items import DmozItem

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://dmoztools.net/Shopping/",
        "http://dmoztools.net/Health/"
    ]

    def parse(self,response):
        for sel in response.xpath('//ul/li'):
            item = DmozItem()
            item['title'] = sel.xpath('a/text()').extract()
            item['link'] = sel.xpath('a/@href').extract()
            item['desc'] = sel.xpath('text()').extract()
            yield item
            #print title,link,desc

        # filename = response.url.split("/")[-2]
        # with open(filename,'wb') as f:
        #     f.write(response.body)
