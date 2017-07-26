#!/usr/bin/python
#-*-coding:UTF-8-*-


# URLError
# import urllib2
# request = urllib2.Request('http://www.123456.com')
# try:
#     urllib2.urlopen(request)
# except urllib2.URLError,e:
#     print e.reason

#HTTPError

import urllib2
req = urllib2.Request('http://blog.csdn.net/cqcre13154')
try:
    urllib2.urlopen(req)
except urllib2.HTTPError,e:
    print e.code
    print e.reason

