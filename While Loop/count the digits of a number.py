# count the digits of a number
num = input("Enter a number:")
a = len(num)
i =1
digits = 0
while i <= a:
    digits += 1
    i += 1
print("The number has",digits,"digits")
input()