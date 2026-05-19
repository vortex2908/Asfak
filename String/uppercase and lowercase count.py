# uppercase and lowercase count
str = input("Enter a string:")
uppercase = 0
lowercase = 0
for i in str:
    if i.isupper():
        uppercase += 1
    else:
        lowercase += 1
print("uppercase letters =", uppercase)
print("lowercase letters =", lowercase)
