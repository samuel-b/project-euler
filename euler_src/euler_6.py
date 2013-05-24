#! bin/bash/python


def factorize(x):
	factorlist = []
	for i in range(2,x):
		if x%i == 0:
			factorlist.append(i)
	return factorlist

factorize(35)
