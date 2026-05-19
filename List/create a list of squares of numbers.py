# create a list of squares of numbers.py
myList = list(eval(input("Enter the elements:")))
squareList = []
for i in myList:
    squareList.append(i**2)
print(squareList)
