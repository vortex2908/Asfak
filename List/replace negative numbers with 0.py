# replace negative numbers with 0.py
myList = list(eval(input("Enter the elements:")))
for i in myList:
    if i < 0:
        index = myList.index(i)
        myList.remove(i)
        myList.insert(index,0)
print(myList)     

