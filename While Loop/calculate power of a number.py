# calculate power of a number
i = 1
num = int(input("Enter a number:"))
pow = int(input("Enter the power for the number:"))
result = 1
while i <= pow:
    result = num **num
    i += 1
print(num,"power",pow,"is",result)
input()
