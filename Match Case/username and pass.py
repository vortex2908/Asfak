# username and pass

username = input("Enter your username")
password = input("Enter your password")

match (username, password):
    case ("Mohamed Asfak", "29082008Aa@"):
        print("Login successful")
    case _:
        print("login unsuccessful")
