# print until 50.py
myList = list(eval(input("Enter the elements:")))
for i in myList:
    if i == 50 :
        print(i,"is found")
        break
    else:
        print(i)
if 50 not in myList:
     print("50 is not found")
