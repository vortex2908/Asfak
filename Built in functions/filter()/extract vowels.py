# extract vowels.py
string = "programming"
vowels = filter(lambda x: x in ['a','e','i','o','u'] ,string)
print(list(vowels))