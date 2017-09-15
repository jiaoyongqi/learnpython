# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

from scrapy.item import Item,Field


class WebCsdnblogItem(Item):
    name = Field()
    url = Field()

class JsonCsdnblogItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    """存储提取信息数据结构"""
    article_name = Field()
    article_url = Field()
    #pass
