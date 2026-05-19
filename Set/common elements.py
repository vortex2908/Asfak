# common elements.py
a = [1,2,3,4,5,1]
b = [1,1,7,8,6,5]

common =  set()

for i in a:
    if a.count(i) > 1 and b.count(i) > 1:
        common.add(i)
print(common)

 