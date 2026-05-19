#Finding weekday or weekend
day = input("Enter a day: ")

match day:
    case day if day in ["Monday","Tuesday","Wednesday","Thursday","Friday"]:
        print("It is a weekday")
    case day if day in ["Sunday","Saturday"]:
        print("It is a Weekend")
    case _:
        pass