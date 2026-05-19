# count number of digits
string = input("Enter a string:")
count = 0
for i in string:
    if i in ("1", "2", "3", "4", "6", "5", "7", "8", "9", "0"):
        count += 1
print("The number of digits in the given string is:", count)
input()
