#!/usr/bin/env python
# -*- coding:utf-8 -*-

li =[50,100,612,1,3,15,69]


#插入排序

for i in xrange(len(li)-1):
	for j in xrange(i+1,len(li)):
		if li[i] <li[j]:
			li[i],li[j]=li[j],li[i]


print li

#如果要改变顺序 改变判断的条件就好了 


