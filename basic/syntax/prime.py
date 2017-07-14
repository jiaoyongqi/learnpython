#!/usr/bin/python
#-*- coding:UTF-8 -*-

#100以内素数  while 实现

i=2
while(i<100):
    j=2
    while(j<=(i/j)):
        if not(i%j):break
        j=j+1
    if(j>i/j): print i," 是素数"
    i = i+1
print "Good bye!"
