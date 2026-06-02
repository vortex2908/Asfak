# even sum.py
from functools import reduce
nums = [1,2,3,4,5,6]
even = filter(lambda x: x % 2 == 0,nums)
sum = reduce(lambda x,y: x +y,even )
print(sum)
