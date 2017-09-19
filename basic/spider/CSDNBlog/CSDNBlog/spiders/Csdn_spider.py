# -*- coding:utf-8 -*-

from scrapy.spider import Spider
from scrapy.http import Request
from scrapy.selector import Selector
from CSDNBlog.items import JsonCsdnblogItem
from CSDNBlog.items import WebCsdnblogItem


class CSDNBlogSpider(Spider):
    """爬CSDN"""
    name = "csdn"#爬虫名,要和settings中的BOT_NAME属性对应的值一致
    # download_delay = 1
    allowed_domains = ["blog.csdn.net"]#搜索的域名范围,也就是爬虫的约束区域,规定爬虫只爬取这个域名下的网页
    start_urls = [
        "http://blog.csdn.net/we1583004we/article/details/77197419"
    ]

    def parse(self,response):
        sel = Selector(response)

        #获得文章url和标题
        #item = JsonCsdnblogItem()
        item = WebCsdnblogItem()

        article_url = str(response.url)
        article_name = sel.xpath('//div[@id="article_details"]/div/h1/span/a/text()').extract()

        # print 0000000000000000
        # print article_name
        # print 0000000000000000
        # item['article_name'] = [n.encode('utf-8') for n in article_name ]
        # item['article_url'] = article_url.encode('utf-8')
        item['name'] = [n.encode('utf-8') for n in article_name]
        item['url'] = article_url.encode('utf-8')

        yield item

        #获得下一篇文章的url
        # urls = sel.xpath('//li[@class="next_article"]/a/@href').extract()
        # for url in urls:
        #     print url
        #     url = "https://blog.csdn.net" + url
        #     print url
        #     yield Request(url,callback=self.parse)




