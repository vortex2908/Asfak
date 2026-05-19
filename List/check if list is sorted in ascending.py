# check if list is sorted in ascending.py
myList = list(eval(input("Enter the elements:")))
ascend = myList[0]
for i in myList:
    if i <= ascend:
        ascend = i
    else:
        print("it is not sorted")
        break
print("it is sorted in ascending order")
        
