# Traffic signal
col = input("Enter a traffic signal colour(Red,Green,Yellow): ")

match col:
    case col if col == "Red":
        print("Stop")
    case col if col == "Green":
        print("Go")
    case col if col == "Yellow":
        print("wait")
    case _:
        print("invalid colour")
