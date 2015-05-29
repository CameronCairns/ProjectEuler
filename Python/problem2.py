#Question:By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
#Once again I will do this the easy way
sum = 0
first = 1
second = 1

while(first<4000000):
  if(first%2 == 0):
    sum+=first
  temporary=first
  first = first+second
  second = temporary

print "The sum of the even terms of the fibonnaci sequence that do not exceed 4 million is:" + sum.__str__()
