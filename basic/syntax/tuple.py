#/usr/bin/python
#-*-coding:UTF-8-*-

'''
python 的元组与列表类似，不同之处在于元组的元素不能修改
元组使用小括号，列表使用方括号
tup1 = ('physics','chemistry',1997)
tup2 = (50,)
tup3 = "a","b","c","d"
'''

tup1 = ('physics','chemistry',1997,2000)
tup2 = (1,2,3,4,5,6,7)

print "tup1[0]: ",tup1[0]
print 'tup2[1:5]: ',tup2[1:5]
'''
执行结果
tup1[0]:  physics
tup2[1:5]:  (2, 3, 4, 5)
'''

# 元组中的元素值是不允许修改的，但是可以对元组进行连接组合
tup1=(12,34,56)
tup2=('abc','xyz')
tup3=tup1+tup2
print tup3
#执行结果 (12, 34, 56, 'abc', 'xyz'）


#删除元组  元组中元素值不允许删除，但是可以删除整个元组
print tup3
del tup3
print "After deleting tup3"
#print tup3
#执行结果 NameError: name 'tup3' is not defined


'''
元组中方法 cmp() 用于比较两个元组元素
cmp(tuple1,tuple2)
返回值

如果比较的元素是同类型的,则比较其值,返回结果。

如果两个元素不是同一种类型,则检查它们是否是数字。

    如果是数字,执行必要的数字强制类型转换,然后比较。
    如果有一方的元素是数字,则另一方的元素"大"(数字是"最小的")
    否则,通过类型名字的字母顺序进行比较。

如果有一个列表首先到达末尾,则另一个长一点的列表"大"。

如果我们用尽了两个列表的元素而且所 有元素都是相等的,那么结果就是个平局,就是说返回一个 0。
'''

tuple1,tuple2 = (123,'xyz'),(456,'abc')
print cmp(tuple1,tuple2)
print cmp(tuple2,tuple1)
tuple3 = tuple2+(786,)
print cmp(tuple2,tuple3)
tuple4=(123,'xyz')
print cmp(tuple1,tuple4)
'''
执行结果
-1
1
-1
0
'''


#tuple()函数将列表转换成元组

aList=[123,'xyz','zara','abc']
aTuple = tuple(aList)
print "Tuple elements : ",aTuple

#执行结果Tuple elements :  (123, 'xyz', 'zara', 'abc')
