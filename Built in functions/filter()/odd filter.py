#odd filter.py
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
odd = filter(lambda x: x % 2 == 1, nums)
print(list(odd))
