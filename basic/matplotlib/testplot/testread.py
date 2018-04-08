#!/usr/bin/python
# coding: utf-8
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

mpl.rcParams['font.family'] = 'sans-serif'
mpl.rcParams['font.sans-serif'] = 'NSimSun,Times New Roman'

x, y = np.loadtxt('test.txt', delimiter=',', unpack=True)
plt.plot(x, y, '*', label='Data', color='black')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Data')
plt.legend()
plt.show()