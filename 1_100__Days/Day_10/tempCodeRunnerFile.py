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
        choice = input(f"Type 'y' to continue calculating with {answer}, or 'n' to start new calculation : ").lower()

        if choice == "y":
            num1 = answer
        elif choice == "n":
            should_accumulate = False
            print("\n"*20)
            calculator()
        else:
            print("Wrong Choice!")

calculator()