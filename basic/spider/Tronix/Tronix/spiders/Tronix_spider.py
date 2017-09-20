# -*- coding:utf-8 -*-

from scrapy.spider import Spider
from scrapy.http import Request
from scrapy.selector import Selector
from Tronix.items import TronixItem


class Tronix_spider(Spider):
    name = "Tronix"
    allowed_domains = ["etherscan.io"]
    start_urls = [
        # "https://etherscan.io/token/generic-tokenholders2?a=0xf230b790e05390fc8295f4d3f60332c93bed42e2&p=1"
        "https://etherscan.io/token/generic-tokenholders2?a=0xf230b790e05390fc8295f4d3f60332c93bed42e2&p={}".format(str(i)) for i in range(1,73)
    ]

    def parse(self,response):
        for sel in response.xpath('//tr'):
            # print sel
            item = TronixItem()
            item['Rank'] = sel.xpath('td[1]/text()').extract_first()
            # print item['Rank']
            item['Address']= sel.xpath('td[2]/span/a/text()').extract_first()
            # print item['Address']
            item['Quantity']=sel.xpath('td[3]/text()').extract_first()
            # print item['Quantity']
            item['Percentage']=sel.xpath('td[4]/text()').extract_first()
            # print item['Percentage']
            print 555555555
            yield item






