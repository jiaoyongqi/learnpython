# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import codecs

class TronixPipeline(object):
    def __init__(self):
        #以可写方式创建并打开存储文件
        print 6666666666
        self.file = codecs.open('Tronix_data.json',mode='wb',encoding='utf-8')

    def process_item(self, item, spider):
        print "jsonjsonjson"
        line = json.dumps(dict(item)) + '\n'  # 转为json格式
        self.file.write(line.decode("unicode_escape"))
        return item

    def spider_closed(self, spider):  # 爬虫结束关闭文件
        self.file.close()
