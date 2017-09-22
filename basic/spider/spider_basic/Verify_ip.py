#-*-coding:UTF-8-*-
import urllib
import socket
'''
验证代理ip是否可用
'''

socket.setdefaulttimeout(3)
f = open("./proxy")
lines = f.readlines()
proxys = []

for i in range(0,len(lines)):
    ip = lines[i].strip("\n").split("\t")
    proxy_host = "http://"+ip[0]+":"+ip[1]
    proxy_tmp = {"http":proxy_host}
    proxys.append(proxy_tmp)

url = "http://ip.chinaz.com/getip.aspx"
for proxy in proxys:
    try:
        res = urllib.urlopen(url,proxies=proxy).read()
        print '******'
        print res
    except Exception,e:
        print '######'
        print proxy
        print e
        continue