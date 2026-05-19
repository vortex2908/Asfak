# printing upto n
i = 1
n = int(input("Enter a number:"))
while i <= n:
    if i %10 ==1:
        print()
    print(i, end=" ")
    i += 1
input()
