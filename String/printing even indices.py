# printing even indices
str = input("Enter a string:")
for i in range(len(str) // 2):
    evenStr = str[::2]
print("The values in even indices are:", evenStr)
