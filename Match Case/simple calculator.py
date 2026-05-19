# This is a simple calculator
a = int(input("Enter a number:"))
b = int(input("Enter another number:"))
operation = input("What arithmatic operation do you want to perform with these: ")

match operation:
    case operation if operation == "sum" | "add" | "addition" | "+" :
        print("The sum of the numbers is:",a+b)
    case operation if operation == "sub" | "difference" | "subtraction" | "-" :
        print("The difference of the numbers is:",a-b)
    case operation if operation == "muliply" | "product" | "x" | "*" :
        print("The product is:",a*b)
    case operation if operation == "divide"| "/" | "div" :
        print("The division of two is:",a/b)
    case _:
        pass
