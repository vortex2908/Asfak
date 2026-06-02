# eligible to vote.py
Age = int(input("Enter Your Age: "))
def voting (a):
    if Age >= 18:
        print("You Are Eligible to Vote")
    else:
        print("You are not Eligible to vote")
voting(Age)
