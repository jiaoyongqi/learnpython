#!/usr/bin/python
# coding: utf-8

import os
import re
import matplotlib.pyplot as plt
import numpy as np

s = []

f = open("test.txt")  # 返回一个文件对象
line = f.readline()  # 调用文件的 readline()方法
while line:
    # print line,  # 后面跟 ',' 将忽略换行符
    lineout=re.split('[,]+',line.strip())
    # print lineout
    for i in range(len(lineout)):
        s.append(float(lineout[i]))
    # print s
    # print(line, end = '')　      # 在 Python 3 中使用
    line = f.readline()

f.close()


# Data for plotting
t = np.arange(0.0, 50.0, 0.1)
# print(t)
# s = 40 + np.sin(2 * np.pi * t)
# print(type(s))
print s
s2=np.array(s)
print s2

# Note that using plt.subplots below is equivalent to using
# fig = plt.figure() and then ax = fig.add_subplot(111)
fig, ax = plt.subplots()
# ax.plot(t, s)

ax.set(xlabel='time (s)', ylabel='voltage (mV)',
       title='About as simple as it gets, folks')
ax.grid()

# fig.savefig("test.png")
plt.show()