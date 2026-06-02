# minimum.py
from functools import reduce

nums = [4, 10, 7, 25, 3]
min = reduce(lambda x, y: min(x, y), nums)
print(min)
