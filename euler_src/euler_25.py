#! bin/bash/python

# find the first fibbonacci number that has 1000 decimal digits
#why won't this work?!

a = 1
b = 1
c = 0
fiblist = []

while len(str(c)) > 0:
	c = a+b
	a = b
	b = c
	fiblist.append(c)

	if len(str(c)) == 1000:
		fiblist.append(c)
		break

#add two because with our algorithm, the first element in fiblist is 2
print(2 + len(fiblist))
