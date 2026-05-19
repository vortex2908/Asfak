# count divisible by 5.py
myList = list(eval(input("Enter the elements:")))
count = 0
for i in myList:
    if i % 5 == 0:
        count += 1
print("there are", count, "elements that are divisible by 5")
