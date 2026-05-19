# set with every element.py
sets = [{1,2,3},{3,4,5},{6,7,8}]
result = set()
for s in sets:
    result = result.union(s)
print(result)
