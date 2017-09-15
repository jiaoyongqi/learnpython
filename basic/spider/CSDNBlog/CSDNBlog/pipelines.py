# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import codecs
from twisted.enterprise import adbapi
import MySQLdb
import MySQLdb.cursors
from logging import log

class JsonCsdnblogPipeline(object):
    def __init__(self):
        #以可写方式创建并打开存储文件
        self.file = codecs.open('CSDNBlog_data.json',mode='wb',encoding='utf-8')

    def process_item(self, item, spider):
        #对item进行处理，并将item写入到json输出文件
        line = json.dumps(dict(item)) + '\n'#转为json格式
        self.file.write(line.decode("unicode_escape"))
        return item

    def spider_closed(self,spider):#爬虫结束关闭文件
        self.file.close()

class WebCsdnblogPipeline(object):
    """保存到数据库中对应的class
        1.在settings.py文件中配置
        2.在自己实现的爬虫类中yield item,会自动执行
    """
    def __init__(self,dbpool):
        self.dbpool = dbpool
        """写死的方式连接线程池,可以从settings配置文件中读取,更加灵活
        self.dbpool=adbapi.ConnectionPool('MySQLdb',
                                          host='127.0.0.1',
                                          db='crawlpicturesdb',
                                          user='root',
                                          passwd='mysql',
                                          cursorclass=MySQLdb.cursors.DictCursor,
                                          charset='utf8',
                                          use_unicode=Fallse)"""

    @classmethod
    def from_settings(cls,settings):
        """1.@classmethod声明一个类方法,平常叫实例方法
           2.类方法中第一个参数cls(class的缩写,指这个类本身),实例方法的第一个参数是self,表示该类的一个实例
           3.可以通过类来调用,类似C.f()
        :param settings:
        :return:
        """
        dbparams=dict(
            host=settings['MYSQL_HOST'],#读取settings中的配置
            db=settings['MYSQL_DBNAME'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASSWD'],
            charset='utf8',#避免中文乱码
            cursorclass=MySQLdb.cursors.DictCursor,
            use_unicode=False,
        )
        dbpool=adbapi.ConnectionPool('MySQLdb',**dbparams)#**表示将字典扩展为关键字参数,相当于 host=xxx,db=yyy...
        return cls(dbpool)#相当于dbpool赋给了这个类,self中可以得到


    #pipeline 默认调用
    def process_item(self,item,spider):
        #进行数据库操作
        query=self.dbpool.runInteraction(self._conditional_insert,item)#调用插入的方法
        query.addErrback(self._handle_error,item,spider)#调用异常处理方法
        return item

    #写入数据库
    def _conditional_insert(self,tx,item):
        print 6666666666666666666666666
        print item['name']
        print item['url']
	print type(item['name'])
	print type(item['url'])
	
        sql="insert into testtable(name,url) values(%s,%s)"
        #sql="insert into testtable(name,url) values('黑熊','垃圾')"
        #sql="insert into testtable(name,url) values('heixiong',laji)"
        #params=(item["name"],item["url"])
	params=(json.dumps(item["name"]),item["url"])
        #params=('heixiong',item["url"])
        #params=('heixiong','2b')
        print 77777777777777777777777777
        #tx.execute(sql)
        tx.execute(sql,params)

    #错误处理方法
    def _handle_error(self,failue,item,spider):
        print '--------database operation exception!!--------'
        print '----------------------------------------------'
        print failue
