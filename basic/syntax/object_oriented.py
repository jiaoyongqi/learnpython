#!/usr/bin/python
#-*-coding:UTF-8-*-


class Employee:
    '所有员工的基类'
    empCount = 0

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print "Total Employee: %d " % Employee.empCount
    def displayEmployee(self):
        print "Name : ",self.name , ", Salary: ",self.salary

"创建 Employee 类的第一个对象"
emp1 = Employee("Zara",2000)
"创建 Employee 类的第二个对象"
emp2 = Employee("Manni",5000)

emp1.displayEmployee()
emp2.displayEmployee()
print "Total Employee %d " % Employee.empCount
'''
执行结果
Name :  Zara , Salary:  2000
Name :  Manni , Salary:  5000
Total Employee 2
'''

#可以添加，删除，修改类的属性
emp1.age = 7 #添加一个'age'属性
emp1.age = 8 #修改'age'属性
#del emp1.age #删除'age'属性

'''
getattr(obj, name[, default]) : 访问对象的属性。
hasattr(obj,name) : 检查是否存在一个属性。
setattr(obj,name,value) : 设置一个属性。如果属性不存在，会创建一个新属性。
delattr(obj, name) : 删除属性。
'''

hasattr(emp1, 'age') # 如果存在 'age' 属性返回 True。
getattr(emp1, 'age') # 返回 'age' 属性的值
setattr(emp1, 'age', 8) # 添加属性 'age' 值为 8
delattr(emp1, 'age') # 删除属性 'age'

'''
__dict__ : 类的属性（包含一个字典，由类的数据属性组成）
__doc__ :类的文档字符串
__name__: 类名
__module__: 类定义所在的模块（类的全名是'__main__.className'，如果类位于一个导入模块mymod中，那么className.__module__ 等于 mymod）
__bases__ : 类的所有父类构成元素（包含了一个由所有父类组成的元组）
'''

print "Employee.__doc__:",Employee.__doc__
print "Employee.__name__:",Employee.__name__
print "Employee.__module__:",Employee.__module__
print "Employee.__bases__:",Employee.__bases__
print "Employee.__dict__:",Employee.__dict__


class Point:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    def __del__(self):
        class_name = self.__class__.__name__
        print class_name,"销毁"

pt1 = Point()
pt2 = pt1
pt3 = pt1
print id(pt1),id(pt2),id(pt3) #打印对象的id
del pt1
del pt2
del pt3

'''
执行结果
3083401324 3083401324 3083401324
Point 销毁
'''
