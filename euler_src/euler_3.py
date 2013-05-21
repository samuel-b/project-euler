#! /bin/bash/python

factorlist = []
product = 1

def factorize (x):
	global product
	for i in range(1,x):
		if (x%i==0):
			factorlist.append(i)
			product *= i
			if product >= x:
				break
	print(factorlist)

#factorize(600851475143)
