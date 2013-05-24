#source code for euler 1
#list sum of all multiples of 3 OR 5 less than 100

myvariable = 0

for i in range(1,1000):
    if (i % 3 == 0) or (i % 5 == 0):
        myvariable += i


print(myvariable)
