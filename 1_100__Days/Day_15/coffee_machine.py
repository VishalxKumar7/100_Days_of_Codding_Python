import sys
import time
from art import cup, MACHINE_FRONT

# **************************************My Code********************************************
# current_resource = {"Water": 300, "Milk": 150, "Coffee": 200}
# Menu = {
#     "espresso": {
#         "ingredients": {
#             "water": 50,
#             "coffee": 18,
#         },
#         "cost": 80
#     },
#     "latte": {
#         "ingredients": {
#             "water": 200,
#             "milk": 150,
#             "coffee": 24
#         },
#         "cost": 100
#     },
#     "cappuccino": {
#         "ingredients": {
#             "water": 250,
#             "milk": 100,
#             "coffee": 24
#         },
#         "cost": 120,
#     }
# }


# resource = True

# def maintenance():
#     restock_resources = input(f"Turn off to restock_resources the machine type 'OFF': ").lower()
#     if restock_resources == "off":
#         return False
#     else:
#         return True

# def amount(choice, payment):
#     return_amount = 0
#     if choice == "espresso" and payment > Menu["espresso"]["cost"]:
#         return_amount = payment - Menu["espresso"]["cost"]
#         return return_amount
#     elif choice == "latte" and payment > Menu["latte"]["cost"]:
#         return_amount = payment - Menu["latte"]["cost"]
#         return return_amount
#     elif choice == "cappuccino" and payment> Menu["cappuccino"]["cost"]:
#         return_amount = payment - Menu["cappuccino"]["cost"]
#         return return_amount
#     elif choice == choice and payment == Menu[choice]["cost"]:
#         return None
#     else:
#         return "collect_money"




# def pay(choice):
#     if choice == "espresso":
#         payment = int(input("You have to pay 80 Rupees. "))
#     elif choice == "latte":
#         payment = int(input("You have to pay 100 Rupees. "))
#     else:
#         payment = int(input("You have to pay 120 Rupees. "))
       
#     payment = amount(choice, payment)
#     if payment == "collect_money":
#         print("Sorry not enough money. Please collect you money")
#     elif payment != None:
#         print(f"Here is your change: {payment}")
#         print(f"Please wait your {choice} is preparing.......")
#         time.sleep(5)
#         print(cup)
#         print(f"\n Please Collect your {choice}")
#         current_resource["Water"] -= Menu[choice]["ingredients"]["water"]
#         current_resource["Coffee"] -= Menu[choice]["ingredients"]["coffee"]
#         if "milk" in Menu[choice]["ingredients"]:
#             current_resource["Milk"] -= Menu[choice]["ingredients"]["milk"]

#     else:
#         print(f"Please wait your {choice} is preparing.......")
#         time.sleep(5)
#         print(cup)
#         print(f"\n Please Collect your {choice}")
#         current_resource["Water"] -= Menu[choice]["ingredients"]["water"]
#         current_resource["Coffee"] -= Menu[choice]["ingredients"]["coffee"]
#         if "milk" in Menu[choice]["ingredients"]:
#             current_resource["Milk"] -= Menu[choice]["ingredients"]["milk"]

    


# def check_current_resource(choice):
#     if choice == "espresso":
#         if Menu["espresso"]["ingredients"]["water"] > current_resource["Water"] and Menu["espresso"]["ingredients"]["coffee"] > current_resource["Coffee"]:
#             print("Sorry there is not enough Water and Coffee!")
#             return maintenance()
#         elif Menu["espresso"]["ingredients"]["water"] > current_resource["Water"]:
#             print("Sorry there is not enough water!")
#             return maintenance()
#         elif Menu["espresso"]["ingredients"]["coffee"] > current_resource["Coffee"]:
#             print("Sorry there is not enough coffee!")
#             return maintenance()
#         else:
#             pay(choice)
#             return True
            
#     else:
#         if Menu[choice]["ingredients"]["water"] > current_resource["Water"] and Menu[choice]["ingredients"]["milk"] > current_resource["Milk"] and Menu[choice]["ingredients"]["coffee"] > current_resource["Coffee"]:
#             print("Sorry there is not enough Water, Milk, and Coffee!")
#             return maintenance()
#         elif Menu[choice]["ingredients"]["water"] > current_resource["Water"]:
#             print("Sorry there is not enough water!")
#             return maintenance()
#         elif Menu[choice]["ingredients"]["milk"] > current_resource["Milk"]:
#             print("Sorry there is not enough Milk!")
#             return maintenance()
#         elif Menu[choice]["ingredients"]["coffee"] > current_resource["Coffee"]:
#             print("Sorry ther is not enough Coffee!")
#             return maintenance()
#         else:
#             pay(choice)
#             return True



# while resource:
#     print(MACHINE_FRONT)
#     choice = input("What would you like? (espresso/latte/cappuccino): ")  
#     resource = check_current_resource(choice)

#*************************************Course Code*******************************************
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 0.80
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24
        },
        "cost": 1.00
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24
        },
        "cost": 1.20,
    }
}

profit = 0
resource = {"water": 300, "milk": 150, "coffee": 200}

def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resource[item]:
            print(f"Sorry ther is not enough {item}.")
            return False
    return True


def process_coins():
    print("Please insert coins.")
    # You must wrap input() in int() to do math
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.10
    total += int(input("how many nickels?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_transaction_sucessfull(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is your change {change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resource[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}")
is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resource['water']}ml")   # Changed 'Water' to 'water'
        print(f"Milk: {resource['milk']}ml")     # Changed 'Milk' to 'milk'
        print(f"Coffee: {resource['coffee']}g")  # Changed 'Coffee' to 'coffee'
        print(f"Money: ${profit}")

    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_sucessfull(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])