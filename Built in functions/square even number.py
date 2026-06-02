# square even number.py
nums = [1,2,3,4,5,6]
even = filter(lambda x: x % 2 == 0,nums)
square = map(lambda x: x**2,even)
print(list(square))
