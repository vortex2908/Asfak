# find maximum and minimum value.py
myTuple = (4,1,8,3)
max = myTuple[0]
min = myTuple[0]
for i in myTuple:
    if i < min:
        min = i
    elif i > max:
        max = i
print("The maximum value:",max)
print("The minimum value:",min)
