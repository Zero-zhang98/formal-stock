#!/usr/bin/env python
# -*- coding:utf-8 -*-

#冒泡排序 
li =[50,100,612,1,3,15,69]

for i in xrange(len(li)-1,1,-1): #此处两个-1分别表示迭代末尾和步长
	#print i
	for j in xrange(i):
		if li[j]>li[j+1]:
			li[j],li[j+1]=li[j+1],li[j]
d[i]=main1
print li


