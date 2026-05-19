# find longest word
sentence = input("Enter a string:")
longest = " "
words = sentence.split()
for i in words:
    if len(longest) < len(i):
        longest = i
print("The longest word is:", longest)
