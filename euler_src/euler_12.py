#! bin/bash/python

#returns a list of factors of the given number
def factorlist(x):
	factorlist = []
	for i in range(2,x):
		if x%i == 0:
			factorlist.append(i)
	return factorlist

#returns the xth triangle number
def triangle(x):
	num = 0
	for i in range(x+1):
		num += i
	return num

fnord = []
incr = 1

while incr > 0:
	if len(factorlist(triangle(incr))) <= 500:
		incr += 1
	elif len(factorlist(triangle(incr))) > 500:
		fnord.append(incr)
		print(incr)
		incr = 0
	else:
		break
