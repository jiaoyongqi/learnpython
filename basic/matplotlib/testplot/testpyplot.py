#!/usr/bin/python
# coding: utf-8
import os
import re
import matplotlib.pyplot as plt
from numpy.random import rand
import numpy as np

x_test = []
y_test = []
# fig, ax = plt.subplots()

fig = plt.figure()
plt.clf() #清除画布
# ax = plt.subplots()
ax = fig.add_subplot(111) #参数的意思是把画布分成1行１列，把图画在第1块（从上到下从左到右数起）。也可以写成 fig.add_subplot(1,1,1)
ax.set_aspect(1) #控制纵横比，1:1

plt.xlim((0,500))
plt.ylim((0,500))

my_x_ticks = np.arange(0,500,10)
my_y_ticks = np.arange(0,500,10)
plt.xticks(my_x_ticks)
plt.yticks(my_y_ticks)
# plt.figure(figsize=(10, 10), dpi=100)

f = open("test.txt")  # 返回一个文件对象
line = f.readline()  # 调用文件的 readline()方法
while line:
    lineout=re.split('[,]+',line.strip())
    x_test.append(float(lineout[0]))
    y_test.append(float(lineout[1]))
    line = f.readline()

f.close()

for color in ['red']:
    scale = 10.0
    ax.scatter(x_test, y_test, c=color, s=scale, label=color,
               alpha=0.3, edgecolors='none')

ax.legend()
ax.grid(True)

plt.show()