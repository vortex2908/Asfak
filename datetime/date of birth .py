from datetime import datetime

def age(a,b):
    Age = int(b[-4:]) - int(a[-4:])
    return Age
def days(c,e):
    past = datetime.strptime(c,"%d-%m-%Y").date()
    present = datetime.strptime(e,"%d-%m-%Y").date()
    return (present - past).days
def leapyear(f):
    if int(f[-4:]) %4 == 0:
        return "your birthday is in a leap year"
    return "Your birthday is not in a leap year"


dob = input('enter your date of birth(DD-MM-YYYY):')
currentdate= input("Enter current date(DD-MM-YYYY):")
print(age(dob,currentdate))
print(days(dob,currentdate))
print(leapyear(dob))