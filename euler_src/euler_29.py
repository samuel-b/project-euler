#euler 29

mylist = []

for i in range(2,101):
    for j in range(2,101):
        if mylist.count(i**j) == 0:
            mylist.append(i**j)

print(len(mylist))
