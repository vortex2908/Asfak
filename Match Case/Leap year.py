# Leap year
year = int(input("Enter a year:"))

match year:
    case leap if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print("It is a leap year")
    case _:
        print("It is not a leap year")
