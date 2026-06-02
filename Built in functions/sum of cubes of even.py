# sum of cubes of even.py
from functools import reduce

nums = [1, 2, 3, 4, 5, 6]
even = filter(lambda x: x % 2 == 0, nums)
cube = map(lambda x: x**3, even)
sum = reduce(lambda x, y: x + y, cube)
print(sum)
