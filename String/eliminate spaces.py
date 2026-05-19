# eliminate spaces
str = input("enter a string:")
newString = ""
for i in str:
    if i == " ":
        continue
    else:
         newString = newString + i
print(newString)           
