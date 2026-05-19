# grading system
mark = int(input("Enter your marks out of 500:"))

match mark:
    case mark if mark >= 400:
        print("Your grade:", "A")
    case mark if mark >= 300 and mark < 400:
        print("Your grade:", "B")
    case mark if mark >= 200 and mark < 300:
        print("Your grade:", "C")
    case mark if mark >= 100 and mark < 200:
        print("Your grade:", "D")
    case mark if mark >= 0 and mark < 100:
        print("You have failed")
    case _:
        print("Invalid mark...!")
