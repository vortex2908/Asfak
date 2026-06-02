# length filter.py
words = ["cat","elephant","dog","tiger"]
length = filter(lambda x: len(x) > 4,words)
print(list(length))