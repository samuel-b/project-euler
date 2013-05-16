#! bin/bash/python

# find the first fibbonacci number that has 1000 decimal digits
#why won't this work?!

a = 1
b = 1
c = 0


while len(str(c)) > 0:
	c = a+b
	a = b
	b = c


	if len(str(c)) == 100:
		print(c)
		break
