# Anagrams
str1 = input("Enter a String:").lower()
str2 = input("Enter a String:").lower()
for i in str1:
    if i not in str2:
        print("it is not a anagram of the other string")
        break
else:
    print("It is a anagram of the other")


