#student data.py
#input 
studentData = []

for i in range(2):
    abcd = {}

    a = (input("Enter your name:"))
    b = (input("Enter your mobile:"))
    c = (input("Enter your email:"))
    d = list(eval(input("Enter your marks in five subjects:")))
    
    abcd.update({"name":a})
    abcd.update({"mobile":b})
    abcd.update({"email":c})
    abcd.update({"marks":d})
    abcd.update({"Total":sum(d)})
    
    studentData.append(abcd)

studentData.sort(key = lambda x : x["Total"] , reverse = True)

print(studentData)