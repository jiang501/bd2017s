#!/usr/bin/env/python
#-*- coding: utf8-*-
if __name__=='__main__':
	n= input()
	array = map(int, raw_input().split())
	max =0
	q = []
	result = 0
	for i in xrange (n-2):
		a = abs(array[i]-array[i+1])+abs(array[i+1]-array[i+2])
		q.append(a)
        if (a > max):
        	max =a 
        	o = i
        else:
        	max =max
	array.pop(o+1)
	for i in xrange (len(array)-1):
    	 result += abs(array[i]-array[i+1])

	print ('result is :%s'% result)