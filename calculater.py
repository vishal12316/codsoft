import math

a = float(input("Enter any number: "))

operators = {
    "+": "addition",
    "-": "subtraction",
    "*": "multiplication",
    "/": "division",
    "sqrt": "square root",
    "pow": "power",
    "%": "modulo"
}

print("Available operators: ", operators)

op = input("Enter the operator: ")

if op in ["+", "-", "*", "/", "%"]:
    b = float(input("Enter another number: "))
    
    if op == "+":
        print(f"{a} + {b} = {a + b}")
    elif op == "-":
        print(f"{a} - {b} = {a - b}")
    elif op == "*":
        print(f"{a} * {b} = {a * b}")
    elif op == "/":
        if b != 0:
            print(f"{a} / {b} = {a / b}")
        else:
            print("Error! Division by zero.")
    elif op == "%":
        print(f"{a} % {b} = {a % b}")
elif op == "sqrt":
    print(f"Square root of {a} = {math.sqrt(a)}")
elif op == "pow":
    b = float(input("Enter the power: "))
    print(f"{a} raised to the power of {b} = {math.pow(a, b)}")
else:
    print("Invalid operator. Please try again.")