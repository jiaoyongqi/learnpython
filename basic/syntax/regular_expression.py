#!/usr/bin/python
#-*-coding:UTF-8-*-

'''
正则表达式是一个特殊的字符序列，它能帮助你方便的检查一个字符串是否与某种模式匹配。
Python 自1.5版本起增加了re 模块，它提供 Perl 风格的正则表达式式。
re 模块使 Python 语言拥有全部的正则表达式功能。
compile 函数根据一个模式字符串和可选的标志参数生成一个正则表达式对象。该对象拥有一系列方法用于正则表达式匹配和替换。
re 模块也提供了与这些方法功能完全一致的函数，这些函数使用一个模式字符串做为它们的第一个参数。

'''


#re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。

import re
print (re.match('www','www.runoob.com').span()) #在起始位置匹配
print (re.match('com','www.runoob.com'))
'''
执行结果
(0, 3)
None
'''

#匹配成功re.match方法返回一个匹配的对象，否则返回None。
#我们可以使用group(num) 或 groups() 匹配对象函数来获取匹配表达式。
'''
group(num=0)	匹配的整个表达式的字符串，group() 可以一次输入多个组号，在这种情况下它将返回一个包含那些组所对应值的元组。
groups()	返回一个包含所有小组字符串的元组，从 1 到 所含的小组号。
'''
line = "Cats are smarter than dogs"
matchObj = re.match(r'(.*) are (.*?) .*',line,re.M|re.I)

if matchObj:
    print "matchObj.group() : ",matchObj.group()
    print "matchObj.group(1) : ",matchObj.group(1)
    print "matchObj.group(2) : ",matchObj.group(2)
else:
    print "No match !!"

'''
执行结果
matchObj.group() :  Cats are smarter than dogs
matchObj.group(1) :  Cats
matchObj.group(2) :  smarter
'''


#re.search 扫描整个字符串并返回第一个成功的匹配

print(re.search('www','www.runoob.com').span())   #在起始位置匹配
print(re.search('com','www.runoob.com').span())   #不在起始位置匹配
'''
执行结果
(0, 3)
(11, 14)
'''

line = "Cats are smarter than dogs"
searchObj = re.search(r'(.*) are (.*?) .*',line, re.M|re.I)
if searchObj:
    print "searchObj.group(): ",searchObj.group()
    print "searchObj.group(1): ",searchObj.group(1)
    print "searchObj.group(2): ",searchObj.group(2)
else:
    print "Nothing found!!"

'''
执行结果
searchObj.group():  Cats are smarter than dogs
searchObj.group(1):  Cats
searchObj.group(2):  smarter
'''

#re.match与re.search的区别
#re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；而re.search匹配整个字符串，直到找到一个匹配。
line = "Cats are smarter than dogs"
matchObj = re.match( r'dogs', line, re.M|re.I)
if matchObj:
    print "match --> matchObj.group() : ", matchObj.group()
else:
    print "No match!!"

matchObj = re.search( r'dogs', line, re.M|re.I)
if matchObj:
    print "search --> matchObj.group() : ", matchObj.group()
else:
    print "No match!!"



'''
检索和替换
Python 的 re 模块提供了re.sub用于替换字符串中的匹配项。
语法：

re.sub(pattern, repl, string, count=0, flags=0)

参数：

    pattern : 正则中的模式字符串。
    repl : 替换的字符串，也可为一个函数。
    string : 要被查找替换的原始字符串。
    count : 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配。
'''

phone = "2004-959-559"  #这是一个国外电话号码
#删除字符串中的Python 注释
num = re.sub(r'#.*$',"",phone)
print "电话号码是： ",num

#删除非数字（-）的字符串
num = re.sub(r'\D',"",phone)
print "电话号码是： ",num
'''
执行结果
电话号码是：  2004-959-559
电话号码是：  2004959559
'''

#repl参数是一个函数
#将匹配的数字乘于2
def double(matched):
    value = int(matched.group('value'))
    return str(value*2)
s = 'A23G4HFD567'
print(re.sub('(?P<value>\d+)',double,s))
#输出结果A46G8HFD1134

'''
正则表达式修饰符 - 可选标志

正则表达式可以包含一些可选标志修饰符来控制匹配的模式。修饰符被指定为一个可选的标志。多个标志可以通过按位 OR(|) 它们来指定。如 re.I | re.M 被设置成 I 和 M 标志：
修饰符	描述
re.I	使匹配对大小写不敏感
re.L	做本地化识别（locale-aware）匹配
re.M	多行匹配，影响 ^ 和 $
re.S	使 . 匹配包括换行在内的所有字符
re.U	根据Unicode字符集解析字符。这个标志影响 \w, \W, \b, \B.
re.X	该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解。
'''
