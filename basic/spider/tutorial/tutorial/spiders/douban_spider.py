#-*-coding:UTF-8-*-

import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from scrapy.spider import BaseSpider
from scrapy.http import Request
from scrapy.selector import HtmlXPathSelector
from tutorial.items import TutorialItem
import re

class DoubanSpider(BaseSpider):
    name = "douban"
    allowed_domains = ["movie.douban.com"]
    start_urls = []

    #从start_urls中读取链接,然后使用make_requests_from_url生成Request
    def start_requests(self):
        #读取含有电影名的文件
        file_object = open('movie_name.txt','r')

        try:
            url_head = "http://movie.douban.com/subject_search?search_text="
            #取每一个电影名构建完整的url,并存放在start_urls中,这个urls用来给
            #make_requests_from_url用
            for line in file_object:
                self.start_urls.append(url_head + line)
            for url in self.start_urls:
                yield self.make_requests_from_url(url)
        finally:
            file_object.close()

    #生成了请求后,scrapy会帮我们处理Request请求,然后获得请求的url的网站的
    #响应response,parse就可以用来处理response的内容
    def parse(self,response):
        hxs = HtmlXPathSelector(response)
        #获得电影的链接
        movie_link = hxs.select('//*[@id="content"]/div/div[1]/div[2]/table[1]/tr/td[1]/a/@href').extract()

        if movie_link:
            #生成request请求后,由我们自定义的方法处理
            yield Request(movie_link[0],callback=self.parse_item)

    #parse_item是我们自定义的方法,用来处理连接的request后获得的response
    def parse_item(self,response):
        hxs = HtmlXPathSelector(response)
        movie_name = hxs.select('//*[@id="content"]/h1/span[1]/text()').extract()
        movie_director = hxs.select('//*[@id="info"]/span[1]/span[2]/a/text()').extract()
        movie_writer = hxs.select('//*[@id="info"]/span[2]/span[2]/a/text()').extract()
        #爬取电影详情需要在已有对象中继续爬取
        movie_description_paths = hxs.select('//*[@id="link-report"]')
        movie_description = []
        for movie_description_path in movie_description_paths:
            movie_description = movie_description_path.select('.//*[@property="v:summary"]/text()').extract()

        #提取演员需要从已有的xPath对象中继续爬我要的内容
        movie_roles_paths = hxs.select('//*[@id="info"]/span[3]/span[2]')
        movie_roles = []
        for movie_roles_path in movie_roles_paths:
            movie_roles = movie_roles_path.select('.//*[@rel="v:starring"]/text()').extract()

        #获取电影详细信息序列
        movie_detail = hxs.select('//[@id="info"]').extract()

        item = TutorialItem()
        item['movie_name'] = ''.join(movie_name).strip().replace(',',';').replace('\'','\\\'').replace('\"','\\\"').replace(':',';')
        #item['movie_link'] = movie_link[0]
        item['movie_director'] = movie_director[0].strip().replace(',',';').replace('\'','\\\'').replace('\"','\\\"').replace(':',';') if len(movie_director) > 0 else ''
        #由于逗号是拿来分割电影所有信息的，所以需要处理逗号;引号也要处理，否则插入数据库会有问题
        item['movie_description'] = movie_description[0].strip().replace(',',';').replace('\'','\\\'').replace('\"','\\\"').replace(':',';') if len(movie_description) > 0 else ''
        item['movie_writer'] = ';'.join(movie_writer).strip().replace(',',';').replace('\'','\\\'').replace('\"','\\\"').replace(':',';')
        item['movie_roles'] = ';'.join(movie_roles).strip().replace(',',';').replace('\'','\\\'').replace('\"','\\\"').replace(':',';')

        #电影详情信息字符串
        movie_detail_str = ''.join(movie_detail).strip()

        yield item

        