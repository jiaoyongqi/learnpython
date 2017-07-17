#!/usr/bin/python
#-*- coding: UTF-8-*-

#读取键盘输入

import os

#raw_input([prompt]) 函数从标准输入读取一个行，并返回一个字符串（去掉结尾的换行符）：
str = raw_input("请输入: ")
print '你输入的内容是： ',str
'''
输出结果：
请输入: 1
你输入的内容是：  1
'''
#input([prompt]) 函数和 raw_input([prompt]) 函数基本类似，但是 input 可以接收一个Python表达式作为输入，并将运算结果返回。
str=input("请输入：")
print "你输入的内容是： ",str
'''
输出结果
请输入：[x*5 for x in range(2,10,2)]
你输入的内容是：  [10, 20, 30, 40]
'''

#打开和关闭文件
fo = open("foo.txt","wb")
print "文件名: ",fo.name
print "是否已关闭: ",fo.closed
print "访问模式： ",fo.mode
print "末尾是否强制加空格：",fo.softspace
fo.write("121324242wwwweweeeee")
fo.close()
fo = open("foo.txt","r+")
str = fo.read(10)
print "读取的字符串是：",str
#tell()方法用于定位文件内的当前位置
position = fo.tell()
print "当前文件位置：",position
#把指针再次定位到文件开头
position = fo.seek(0,0)
str=fo.read(10)
print "重新读取字符串：",str
fo.close()

#重命名文件
os.rename("foo.txt","foo1.txt")
#删除一个已经存在的文件
os.remove("foo1.txt")

#显示当前的工作目录
print os.getcwd()
