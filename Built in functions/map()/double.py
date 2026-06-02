#map()

List = eval(input("Enter a number:"))
def double (x):
    return x * 2
result = (map(double,List))
print(list(result))