# divisible by 5.py

divBy5 = int(input("Enter a number: "))

def divisible (a):
    if a % 5 == 0:
        print("Divisible by 5")
    else:
        print("Not divisible by 5")
divisible(divBy5)
