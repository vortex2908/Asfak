# replace vowels
str = input("Enter a string:")
newStr = ""
for i in str:
    if i in ("aeiouAEIOU"):
        newStr += "*"
    else:
        newStr += i
print(newStr,"all vowels are replaced with <*>")
