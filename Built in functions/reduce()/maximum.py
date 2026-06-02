# maximum.py
from functools import reduce

nums = [4, 10, 7, 25, 3]
max = reduce(lambda x, y: max(x, y), nums)
print(max)
