#!/usr/bin/env/python
#-*- coding: utf8-*-
class Point():
	def __init__(self,l):
		self.c= l[0]
		self.x=int(l[1])
		self.y=int(l[2])
		self.z=int(l[3])
class ways():
	def __init__(self,l):
		self.l = l
	def zhuti(self,n):
		i,j,k=0,1,2
		max =0
		for i in range(n):
			for j in range(i+1,n):
				for k in range(j+1,n):
					if self.sanjiaoxing(i,j,k) and self.color(i,j,k):
						Area = self.mianji(i,j,k)
						if max<Area:
							max = Area
		return max
	def color (self,i,j,k):
		if self.l[i].c==self.l[j].c and self.l[j].c ==self.l[k].c:
			return True
		elif self.l[i].c !=self.l[j].c and self.l[j].c !=self.l[k].c and self.l[i].c !=self.l[k].c:
			return True
		return False
	def sanjiaoxing(self,i,j,k):
		a=self.length(i,j)
		b=self.length(i,k)
		c=self.length(j,k)
		if a <b+c and b<a+c and c<a+b :
			return True
		return False
	def length(self,i,j):
		x= abs(self.l[i].x-self.l[j].x)
		y= abs(self.l[i].y-self.l[j].y)
		z = abs(self.l[i].z-self.l[j].z)
		return (x*x+y*y+z*z)**0.5
	def mianji(self,i,j,k):
		a = self.length(i,j)
	 	b = self.length(i,k)
		c= self.length(j,k)
		s = (a+b+c)/2
		area = (s*(s-a)*(s-b)*(s-c))**0.5
		return area
if __name__=='__main__':
	n = input()
	l = []
	for i in range(n):
		string = raw_input().split()
		node = Point(string)
		l.append(node)
	s = ways(l)
	print("%.5f"%s.zhuti(n))
