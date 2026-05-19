name = input("Enter a string:")
vowels = 0
for i in name:
    if i in ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U"):
        vowels += 1
print(vowels)
