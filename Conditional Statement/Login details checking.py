# Login details checking

crtGmail = "abcd@gmail.com"
crtPass = "2908Aa@"
inpGmail = input("Enter your Gmail:")
inpPass = input("Enter your password:")
if crtGmail == inpGmail:
    if crtPass == inpPass:
        print("Login Successful")
    else:
        print("Incorrect Password")
else:
    print("Incorrect Gmail")
    print("Login unsuccessful")
