myDict = {
    "name": "Mohamed Asfak",
    "mobile": 8056657403,
    "age": 15,
    "email": "mohamedasfak123@gmail.com",
    "age": 17,
}

# ordered, mutable ( changable ), Unique Keys
print(myDict)
print(type(myDict))


# accessing
print(myDict["email"])
print(myDict.get("name"), "name of the user")
print(myDict.get("total"))  # if the key doesn't exist, avoiding errors.
# print(myDict["total"])     # if the key doesn't exist, errors found.

print(len(myDict))

print(myDict.keys())

print(myDict.values())

print(myDict.items())

myDict["mobile"] = 9789491350
print(myDict)

myDict.update({"rank": "4"})
print(myDict)

keys = ("name", "age", "job")
new_dict = dict.fromkeys(keys)
print(new_dict)


del myDict["age"]
print(myDict)


# pop()


studentsData = [
    {
        "name": "Thanushwar",
        "mobile": 8937823535,
        "email": "thanushwar123@gmail.com",
        "age": 17, 
    },
    {
        "name": "Roobasri",
        "mobile": 1234567890,
        "email": "Roobasri123@gmail.com",
        "age": 17,
    },
    {
        "name": "Srinivasan",
        "mobile": 1234567890,
        "email": "Srinivasan123@gmail.com",
        "age": 17,
    },
]

print(studentsData)
print(studentsData[1])
print(studentsData[1]["email"])


for i in studentsData:
    print(i, "student data")
