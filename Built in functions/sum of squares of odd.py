# sum of squares of odd.py
from functools import reduce
nums = [1,2,3,4,5]
odd = filter(lambda x : x % 2 !=0,nums)
square = map(lambda x : x**2 , odd)
sum = reduce(lambda x,y: x + y,square)
print(sum) 

