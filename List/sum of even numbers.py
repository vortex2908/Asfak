# sum of even numbers.py
myList = list(eval(input("Enter the elements:")))
sum = 0
for i in myList:
    if i % 2 == 0:
        sum += i
print(sum)
