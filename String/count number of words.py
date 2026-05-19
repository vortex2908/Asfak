# count number of words
sentence =  input("Enter a string:").strip()
words = 1
for i in sentence:
    if i == " ":
        words += 1
print("The number of words in string:", words)
