# count postive and negative numbers.py
myList = list(eval(input("Enter the elements:")))
positiveDig = 0
negativeDig = 0
zero = 0
if len(myList) > 0: 
    for i in myList:
        if i > 0 :
            positiveDig += 1
        elif i < 0 :
            negativeDig += 1
        else:
            zero += 1 
else:
    print("It is an empty list")
print("The number of postive numbers:",positiveDig)
print("The number of negative numbers:",negativeDig)
print("The number of zeros:",zero)
