#/usr/bin/python
#-*-coding:UTF-8-*-

#python 访问字符串中的值
var1 = 'Hello World'
var2 = "Python Runoob"

print "var1[0]: ",var1[0]
print "var2[1:5]: ",var2[1:5]

#字符串更新
print "更新字符串：- ", var1[:6] + 'jyqi!'


#原始字符串
print r'\n'
print R'\n'

#字符串格式化 最基本的用法是将一个值插入到一个有字符串
#格式符%s 的字符串中
print "My name is %s and weight is %d kg!" % ('zara',21)
