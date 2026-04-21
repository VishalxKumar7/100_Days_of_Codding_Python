"""
Calculator for pizza order
Small pizza = $15
Medium Pizza = $ 20
Large pizza = $ 25
Add pepperoni for small (Y or N): +$2
Add pepperoni for medium and large (Y or N): +$3
Add extra cheese for any size pizza (Y or N): +$1
"""

print("Weolocme to Pyton Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

bill = 0

if size == "S":
    bill = 15
    print("You have selected the Small Pizza")
elif size == "M":
    bill = 20
    print("You have selected Medium Pizza")
elif size == "L":
    bill = 25
    print("You have selected Large Pizza")
else:
    print("You typed the wront input.")

# Adding Pepperoni
if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
    print("Pepperoni Added")

# Adding Extra Cheese
if extra_cheese == "Y":
    bill += 1
    print("Extra cheese Added")

print(f"Your Total Bill is {bill}")