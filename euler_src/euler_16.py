#project euler 16


mytuple = tuple(str(2**1000))
mysum = 0

for object in mytuple:
    mysum += int(object)

print(mysum)
