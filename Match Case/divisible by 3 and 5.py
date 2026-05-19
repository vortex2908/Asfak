# divisible by 3 and 5

num = int(input("Enter a number:"))
match num:
    case divisible if num % 3 == 0 and num % 5 == 0:
        print("The number is divisible by both 3 and 5")
    case _:
        print("The number is not divisible by both 3 and 5")
