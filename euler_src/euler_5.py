#! /bin/bash/python

max_divisor = 20
num = 2520
state = False

def is_divis (number, max_divisor):
    for i in range(max_divisor,0,-1):
        if number % i != 0:
            #returns false on first divisor that has a nonzero remainder
            return False
    #returns true if every number in range divides input num evenly
    return True

# checks if num is evenly divisible by our specified range. if not, num += 1 and check again. If num is evenly divisible by our range, it prints that number and exits. 
while state == False:
    if is_divis(num, max_divisor) == True:
        print(num)
        state = True
    else:
        num += 1
