#print second largest.py
myList = list(eval(input("Enter the elements:")))
largest = myList[0]
secLarge = myList[0]
for i in myList:
    if i > largest :
        secLarge = largest
        largest = i
    elif i  > secLarge and i != largest:
        secLarge = i
print(secLarge,"is the second largest number")