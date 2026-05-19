# lie between 1 and 10
num = int(input("Enter a number:"))
match num:
    case true if num > 1 and num < 10:
        print("The number lies between 1 and 10")
    case _:
        print("The number does not lie between 1 and 10")
