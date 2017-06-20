#!/usr/bin/env/python
#-*- coding: utf8-*-
if __name__=='__main__':
	n  = input()
	array = map(int,raw_input().split())
	a = []
	a = sorted(array)
	k =0
	j=0
	for i in range(n):
		if array[i]==a[j]:
			k +=1
			j+=1
	result = n - k
	print ('time is %s'%result)


