#/usr/bin/python
#-*-coding:UTF-8-*-

#访问列表中的值
list1 = ['physics','chemistry',1997,2000]
list2 = [1,2,3,4,5,6,7]

print "list1[0]: ",list1[0]
print 'list2[1:5]: ', list2[1:5]
print 'list1[-2]: ',list1[-2]

#更新列表
print "Value available at index 2: "
print list1[2]
list1[2]=2001
print "New value available at index 2:"
print list1[2]

#删除列表元素
print list1
del list1[2]
print "After deleting value at index 2:"
print list1

#python 列表操作符
#列表+号用于组合列表，*号用于重复列表
