#-*-coding:UTF-8-*-
import urllib2
from bs4 import BeautifulSoup

'''
获取代理 ip
'''

User_Agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0'
header = {}
header['User-Agent'] = User_Agent

url = 'http://www.xicidaili.com/nn/1'
req = urllib2.Request(url,headers=header)
res = urllib2.urlopen(req).read()

soup = BeautifulSoup(res)

#print soup

ips = soup.findAll('tr')
f = open("./proxy","w")

for x in range(1,len(ips)):
    ip = ips[x]
    tds = ip.findAll('td')
    #print tds
    #print tds[1].contents[0]
    ip_temp = tds[1].contents[0]+"\t"+tds[2].contents[0]+"\n"
    print tds[1].contents[0]+"\t"+tds[2].contents[0]+"\n"
    f.write(ip_temp)
