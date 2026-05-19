# ATM machine
crtAccNo = 1234567891011121
crtPin = 1111
savings = 30000

inpAccNo = int(input("Enter Your Account Number:"))
inpPin = int(input("Enter Your Pin:"))

if crtAccNo == inpAccNo:
    if crtPin == inpPin:
        inpAmnt = int(input("Enter the needed amount:"))
        if savings >= inpAmnt:
            print("The cash is successfully withdrawn")
        else:
            print("Insufficient Funds")
    else:
        print("Incorrect Pin, please try again")
else:
    print("incorrect Account Number")
