# print duplicate values.py
myList = list(eval(input("Enter the elements:")))
duplicate = []
for i in myList:
    a = myList.count(i)
    if a > 1:
        duplicate.append(i)
print(list(set(duplicate)))
