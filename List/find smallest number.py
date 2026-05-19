# find smallest number.py

list = list(eval(input("Enter the elements:")))
smallest = list[0]
for i in list:
    if i < smallest:
        smallest = i
print("The smallest number :",smallest)
