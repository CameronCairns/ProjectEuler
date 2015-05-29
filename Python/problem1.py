#Question:Find the sum of all the multiples of 3 or 5 below 1000.
#All multiples of 3 or 5 are congruent to itself modulo 3 or 5

#Easy way to do this go from 1 to 1000 and see what numbers are congruent modulo 3 or 5
sum = 0
for i in range(1, 1000):
  if (i%3==0 or i%5==0):
    sum+=i
print "The sum of all numbers that are multiples of 3 or 5 that are below 1000 is:" + sum.__str__() 
