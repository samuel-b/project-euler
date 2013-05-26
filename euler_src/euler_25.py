#! bin/bash/python

# find the first fibbonacci number that has 1000 decimal digits

a,b = 0,1
c = 0
fiblist = [1,]
count = 1

while len(str(c)) > 0:
	c = a+b
	a,b = b,c
	fiblist.append(c)
	count += 1

	if len(str(c)) == 1000:
		print(count)
		break
