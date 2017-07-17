#!/usr/bin/python
#-*-coding:UTF-8-*-

#字典的每个键值(key=>value)对用冒号(:)分割，每个对之间用逗号(,)分割，整个字典包括在花括号({})中 ,格式如下所示：
# d = {key1 : value1, key2 : value2 }

#访问字典里的值
dict={'Name':'Zara','Age':7,'Class':'First'}
print "dict['Name']: " ,dict['Name']
print "dict['Age']: ",dict['Age']
'''
执行结果：
dict['Name']:  Zara
dict['Age']:  7
'''
#修改字典   向字典添加新内容的方法是增加新的键/值对，修改或删除已有键/值对如下实例:
dict['Age']=8
dict['School']='DPS School'
print "dict['Age']: ",dict['Age']
print "dict['School']: ",dict['School']
'''
执行结果
dict['Age']:  8
dict['School']:  DPS School
'''
#删除字典元素 能删单一的元素也能清空字典

del dict['Name'] #删除键是'Name'的条目
dict.clear()  #清空词典所有条目
del dict  #删除词典


'''
字典键的特性
1）不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住
2）键必须不可变，所以可以用数字，字符串或元组充当，所以用列表就不行，
'''


#字典 str() 方法
dict = {'Name':'Zara','Age':7}
print 'Equivalent String: %s ' % str(dict)

#执行结果 Equivalent String: {'Age': 7, 'Name': 'Zara'} 
