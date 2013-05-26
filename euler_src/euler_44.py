# return the nth pentagonal number
def pentagonal(x):
    return ((x*(3*x-1))//2)

#generate a list of pentagonals for brute forcing

pentags, pentags2  = [], []
for i in range(1000,10000):
    pentags.append(pentagonal(i))
    pentags2.append(pentagonal(i))


for item in pentags:
    for item2 in pentags2:
        if (pentags.count(item + item2) != 0) and (pentags.count(item2 - item) != 0):
            print(item,' ',item2,' ',abs(item2-item))
            break
            
        
