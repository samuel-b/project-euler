#! bin/bash/python

#project euler problem 4
#find the largest palindromic number that is the product of two 3 digit ints. 

sixdig = []
palindromes = []

for i in range(100,1000):
    for j in range (100,1000):
        intstr = str(i*j)
        reverse = intstr[::-1]
        if intstr == reverse:
            palindromes.append(intstr)

for object in palindromes:
    if len(str(object)) == 6:
        sixdig.append(object)

sixdig.sort()
print(sixdig)
