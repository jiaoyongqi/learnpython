#/usr/bin/python
#-*-coding:UTF-8-*-

#for 实现素数

for i in range(2,101):
    fg=0
    for j in range(2,i/2+1):
        if i%j==0:
            fg=1
            break
    if fg == 0:
        print i," 是素数"
