#count even and odd numbers.py
myList = eval(input("enter the elements:"))
even = 0
odd = 0
for i in myList:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print("Even numbers:",even)
print("Odd numbers:",odd)
