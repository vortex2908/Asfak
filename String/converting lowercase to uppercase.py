# converting lowercase to uppercase
str = input("Enter a string:")
up = ""
for i in str:
    if "a" <= i <= "z":
        up += chr(ord(i )- 32)
    else:
        up = +i
print(up)
