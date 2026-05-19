# find largest number.py
list = list(eval(input("Enter the elements:")))
biggest = 0
for i in list:
    if i > biggest:
        biggest = i
print("The largest number :",biggest)