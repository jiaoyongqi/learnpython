#/usr/bin/python
#-*-coding:UTF-8-*-

#list 方法

#list.append(obj)  在列表末尾添加新的对象
aList = [123,'xyz','zara','abc']
aList.append(2009)
print "Updated List :",aList

# 结果 Updated List : [123, 'xyz', 'zara', 'abc', 2009]

#list.count(obj) 统计某个元素在列表中出现的次数

aList.append('zara')
print "Count for 123: ",aList.count(123)
print "Count for zara: ",aList.count('zara')

'''
执行结果
Updated List : [123, 'xyz', 'zara', 'abc', 2009]
Count for 123:  1
Count for zara:  2
'''

#list.extend(obj)用于在列表末尾一次性追加另一个序列中的多个值(用新列表扩展原来的列表)
bList=[2009,'manni']
aList.extend(bList)
print "Extend List: ",aList

#执行结果 Extend List:  [123, 'xyz', 'zara', 'abc', 2009, 'zara', 2009, 'manni']

#list.index(obj) 从列表中找出某个值第一个匹配项的索引位置
print "Index for xyz: ",aList.index('xyz')
print "Index for zara: ",aList.index('zara')
'''
执行结果
Index for xyz:  1
Index for zara:  2
'''

#list.insert(index,obj) 将指定对象插入列表的指定位置
aList.insert(3,2009)
print "insert Final List: ",aList
# 执行结果insert Final List:  [123, 'xyz', 'zara', 2009, 'abc', 2009, 'zara', 2009, 'manni']

#list.pop(obj=list[-1])
#移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
print "before pop aList: ",aList
print "A List pop: ",aList.pop()
print "after pop aList: ",aList
print "B List pop(2) ",aList.pop(2)
print "after pop(2) aList: ",aList

'''
执行结果
before pop aList:  [123, 'xyz', 'zara', 2009, 'abc', 2009, 'zara', 2009, 'manni']
A List pop:  manni
after pop aList:  [123, 'xyz', 'zara', 2009, 'abc', 2009, 'zara', 2009]
B List pop(2)  zara
after pop(2) aList:  [123, 'xyz', 2009, 'abc', 2009, 'zara', 2009]
'''

#list.remove(obj) 移除列表中某个值的第一个匹配项
print "Before remove aList: ",aList
aList.remove('xyz')
print "after remove xya aList:",aList
aList.remove(2009)
print "after remove 2009 aList:",aList

'''
执行结果
Before remove aList:  [123, 'xyz', 2009, 'abc', 2009, 'zara', 2009]
after remove xya aList: [123, 2009, 'abc', 2009, 'zara', 2009]
after remove 2009 aList: [123, 'abc', 2009, 'zara', 2009]
'''

#list.reverse() 用于反向列表中元素
print "Before reverse aList: ",aList
aList.reverse()
print "after reverse aList: ",aList
'''
执行结果
Before reverse aList:  [123, 'abc', 2009, 'zara', 2009]
after reverse aList:  [2009, 'zara', 2009, 'abc', 123]
'''

#list.sort([func]) 对原列表进行排序，如果指定参数，则使用比较函数指定的比较函数
print "Before soft aList: ",aList
aList.sort()
print "After soft aList: ",aList
'''
执行结果
Before soft aList:  [2009, 'zara', 2009, 'abc', 123]
After soft aList:  [123, 2009, 2009, 'abc', 'zara']
'''
