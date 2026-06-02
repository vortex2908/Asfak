# count words.py
words = ["cat","apple","dog","banana"]
a = filter(lambda x : len(x) > 3,words)
print(len(list(a)))