#!/usr/bin/env/python
#-*- coding: utf8-*-
import numpy as np
if __name__=='__main__':
	a = map(int,raw_input().split())
	n = a[0]
	k = a[1]
	dp = np.zeros((1000,1000),dtype = np.int)
	dp[1][0]=1
	for i in range(2,(n+1)):
		for j in range(n):
			if j ==0:
				dp[i][j]=1
			else:
				dp[i][j]=(dp[i-1][j-1]*(i-j)+dp[i-1][j]*(j+1))%2017
	print('result%s'%dp[n][k])