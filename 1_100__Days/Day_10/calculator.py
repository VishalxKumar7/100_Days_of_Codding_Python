### CALCULATOR APP
import sys
from art import logo
print(logo)

### MY CODE
# def calculator(num1, operator, num2):

#     if operator == "+":
#         return num1 + num2
#     elif operator == "-":
#         return num1 - num2
#     elif operator == "*":
#         return num1 * num2
#     elif operator == "/":
#         return num1/num2
#     else:
#         print("Wrong Choice!")

# num1 = float(input("Enter the number: "))
# operator = input("Pick an operation +, -, *, /: ")
# num2 = float(input("Enter the number: "))
# result = 0
# should_continue = True
# result = calculator(num1, operator, num2)

# while should_continue:
#     continue_or_not = input(f"Current result {result} Enter the 'y' if you want to continue to perform calculation else 'n': ").lower()
    
#     if continue_or_not == "n":
#         should_continue = False
#         print(f"\n {result}")
#     elif continue_or_not == "y":  
#         operator = input("Enter you want to perform +, -, *, /: ")
#         num2 = float(input("Enter the number: "))
#         result = calculator(num1=result, operator=operator, num2=num2)
#     else:
#         print("Wrong Choice!")

# ********************************************************************************************

# COURSE CODE
def add(n1, n2):
    return n1 + n2

def substact(n1,n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def devide(n1, n2):
    return n1 / n2

operations  = {"+": add, "-": substact, "*": multiply, "/": devide}

# print(operations["*"](3,4))
def calculator():
    should_accumulate = True
    num1 = float(input("Enter the number: "))

    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operator = input("Pick an operation: ")
        num2 = float(input("Enter the number: "))
        answer = operations[operator](num1, num2)
        print(f"{num1} {operator} {num2} = {answer}")
        choice = input(f"Type 'y' to continue calculating with {answer}, or 'n' to start new calculation, to 'exit' enter exit: ").lower()

        if choice == "y":
            num1 = answer
        elif choice == "n":
            should_accumulate = False
            print("\n"*50)
            calculator()
        elif choice == "exit":
            print("GoodBye!")
            sys.exit()
        else:
            print("Wrong Choice!")

calculator()