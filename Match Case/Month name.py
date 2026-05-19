# finding month name
month = int(input("Enter a month number:"))
match month:
    case month if month == 1:
        print("January")
    case month if month == 2:
        print("February")
    case month if month == 3:
        print("March")
    case month if month == 4:
        print("April")
    case month if month == 5:
        print("May")
    case month if month == 6:
        print("June")
    case month if month == 7:
        print("July")
    case month if month == 8:
        print("August")
    case month if month == 9:
        print("September")
    case month if month == 10:
        print("October")
    case month if month == 11:
        print("November")
    case month if month == 12:
        print("December")
    case _:
        print("Invalid month number!!!")
