# pass or fail.py

mark = int(input("Enter your mark: "))

def pass_fail(a):
    if a >= 50:
        print("You have passed")
    else:
        print("You have failed")
pass_fail(mark)
