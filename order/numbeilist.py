#!/usr/bin/env python
# -*- coding:utf-8 -*-

#选择排序 
'''
#下面这段代码本质是冒泡排序
nuum=[21,65,5,101,78,32,250]
l=len(nuum)
for i in xrange(l-1):
    for j in xrange(i,l-1):
        if nuum[i]>nuum[j]:
            nuum[j],nuum[i]=nuum[i],nuum[j]
            print nuum
print nuum
'''
'''
q=[95,15,3,57,109,85,77]
for i in range(len(q)):
    for j in range(i+1,len(q)):
        if q[j]<q[i]:
            q[i],q[j]=q[j],q[i] 
            print q  

print('dshajkflskajfk')
'''

#冒泡排序，简而言之，就是不断地将最大的数靠后排列
'''
num=[45,66,37,89,21,7,9,15]
n=len(num)p
for i in range(n-1): #确定循环的次数
    for j in range(n-i-1): #确定循环的下标
        if num[j]>num[j+1]:
            num[j],num[j+1]=num[j+1],num[j]
            print num
print num
'''

#插入排序
'''
p=[10,35,99,15,5,97]
for x in range(1,len(p)):
    for i in range(x-1,-1,-1):
        #print i,
        if p[i]>p[i+1]:
            p[i],p[i+1]=p[i+1],p[i]
            print p
print p 
'''

#快速排序







    


