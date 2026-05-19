# count special characters
str = "asfak ^&*"#input("Enter a string:")
count = 0
for i in str:
    if i.isalpha and i.isnumeric:
        var = 0
    else:
        count += 1
print(count)
