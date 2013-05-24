#problem 6
# for the first 100 natural numbers, find the difference between the square of the sum and the sum of the square. 


#numbers up to and including 100
sum_sqrs = 0
sum_digits = 0
for i in range(101):
	#add i to sum_digits
	sum_digits += i
	#square i and then add it to sum_sqrs
	sum_sqrs += i**2

#square the sum of the digits
sum_squared = sum_digits**2

#print the desired difference
print(sum_squared - sum_sqrs)
