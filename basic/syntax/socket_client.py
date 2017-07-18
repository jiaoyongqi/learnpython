#!/usr/bin/python
#-*-coding:UTF-8-*-

import socket       #导入socket 模块

s = socket.socket()    #创建socket 对象
host = socket.gethostname()     #获取本地主机名
port = 12345            #设置好端口

s.connect((host,port))
print s.recv(1024)
s.close
