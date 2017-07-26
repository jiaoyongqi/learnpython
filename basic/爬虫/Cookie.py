#!/usr/bin/python
#-*-coding:UTF-8-*-

#1)利用CookieJar对象实现获取cookie的功能,存储到变量中
import urllib2
import cookielib

#声明一个CookieJar对象实例来保存cookie
cookie = cookielib.CookieJar()
#利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
handler = urllib2.HTTPCookieProcessor(cookie)
#通过handler来构建opener
opener = urllib2.build_opener(handler)
#此处的open方法同urllib2的urlopen方法，也可以传入request
response = opener.open('http://www.baidu.com')
for item in cookie:
    print 'Name = '+item.name
    print 'Value = '+item.value


#2)保存Cookie到文件,使用FileCookieJar
import cookielib
import urllib2

#设置保存cookie的文件,同级目录下的cookie.txt
filename = 'cookie.txt'
#声明一个MozillaCookieJar对象实例来保存cookie,之后写入文件
cookie = cookielib.MozillaCookieJar(filename)
#利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
handler = urllib2.HTTPCookieProcessor(cookie)
#通过handler来构建opener
opener = urllib2.build_opener(handler)
#创建一个请求,原理同urllib2的urlopen
response = opener.open("http://www.baidu.com")
#保存cookie到文件
cookie.save(ignore_discard=True,ignore_expires=True)
'''
ignore_discard的意思是即使cookies将被丢弃也将它保存下来，
ignore_expires的意思是如果在该文件中 cookies已经存在，
则覆盖原文件写入，在这里，我们将这两个全部设置为True。运行之后，
cookies将被保存到cookie.txt文件中
'''


#3)从文件中获取Cookie并访问
import cookielib
import urllib2

#创建MozillaCookieJar实例对象
cookie = cookielib.MozillaCookieJar()
#从文件中读取cookie内容到变量
cookie.load('cookie.txt',ignore_discard=True,ignore_expires=True)
#创建请求的request
req = urllib2.Request("http://www.baidu.com")
#利用urllib2的build_opener方法创建一个opener
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
response = opener.open(req)
print response.read()


#4)利用cookie模拟网站登录
#参考例子
import urllib
import urllib2
import cookielib

filename = 'cookie.txt'
#声明一个MozillaCookieJar对象实例保存cookie,之后写入文件
cookie = cookielib.MozillaCookieJar(filename)
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
postdata = urllib.urlencode({
        'stuid':'2013123122',
        'pwd':'1242142'
    })
#登录教务系统的URL
loginUrl = 'http://jwxt.sdu.edu.cn:7890/...../login'
#模拟登录,并把cookie保存到变量
result = opener.open(loginUrl,postdata)
#保存cookie到cookie.txt中
cookie.save(ignore_discard=True,ignore_expires=True)
#利用cookie请求访问另一个网址,此网址是成绩查询网址
gradeUrl = 'http://jxwt.std.edu.cn:7890/.../'
#请求访问成绩查询网址
result = opener.open(gradeUrl)
print result.read()

'''
以上程序的原理如下
创建一个带有cookie的opener，在访问登录的URL时，将登录后的cookie保存下来，然后利用这个cookie来访问其他网址。
如登录之后才能查看的成绩查询呀，本学期课表呀等等网址，模拟登录就这么实现
'''