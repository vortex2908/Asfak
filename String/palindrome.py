# palindrome
str = input("Enter a string to reverse:")
rev = ""
for i in str:
    rev = i + rev
print(rev)
if rev == str:
    print("It is a palindrome")
else:
    print("It is not a palindrome")
