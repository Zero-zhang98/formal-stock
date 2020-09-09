#!/usr/bin/env python
# -*- coding:utf-8 -*-

li =[50,100,612,1,3,15,69]

#选择排序

for i in range(len(li)):
	position =i
	for j in range(i,len(li)):
		if li[position] <li[j]:
			position =j
	if position !=i:
		# tem =li[position]
		# li[position] =li[i]
		# li[i]=tem
		li[position],li[i] =li[i],li[position] #用这种更快 更简洁
		print (li)
print (li)


#插入 冒泡 选择 希尔 归并 堆 快速