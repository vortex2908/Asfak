# Age group
Age = int(input("Enter your age:"))

match Age:
    case child if Age > 3 and Age <= 12:
        print("Age group: Child")
    case teen if Age > 12 and Age <= 19:
        print("Age group: Teen")
    case adult if Age > 19 and Age <= 64:
        print("Age group: Adult")
    case _:
        print("Age group: Senior")
