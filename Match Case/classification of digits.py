# classification of digits
n = int(input("Enter a number:"))

match n:
    case pos_odd if n > 0 and n % 2 != 0:
        print("The number is positive odd")
    case pos_even if n > 0 and n % 2 == 0:
        print("The number is positive even")
    case negative if n < 0:
        print("The number is negative")
    case _:
        print("The number is zero")
