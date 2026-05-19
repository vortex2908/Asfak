# check to see if containing only alphabet
str = input("Enter a string")
for i in str:
    if i not in ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        print("It contains characters other than alphabet")
        break
else:
    print("It only contains alphabets")
