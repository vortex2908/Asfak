# check if palindrome
strings = {"mad","am"}
a = ""
for i in strings:
    a = a + i
print(a)
rev = ""
for s in a:
    rev =  s + rev
print(rev)
if a == rev:
    print("It is a palindrome")
else :
    print("It is not a palindrome") 
