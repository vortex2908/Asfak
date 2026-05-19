no = int(input("Enter a number:"))

match no:
    case no if no % 2 == 0:
        print("The given number is even")
    case _:
        print("The given number is odd")    
