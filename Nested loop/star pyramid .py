# simple * pattern pyramid
rows = 5#int(input("Enter a number:"))
for i in range(1,rows+1):
    for j in range(rows-1):
        print()
    for k in range(i*2-1):
        print("*",end = " ")
