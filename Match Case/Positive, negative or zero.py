integer = int(input("Enter a number:"))
match integer:
    case integer if integer > 0:
        print("The number is positve")
    case integer if integer < 0:
        print("The number is negative")
    case _:
        print("The number is zero")
