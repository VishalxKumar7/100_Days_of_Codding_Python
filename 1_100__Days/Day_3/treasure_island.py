print("Welcome to Treasure Island")
print("Your mission is to find the treasure.")
choice1 = input("You're at a crossroad, where do you want to go? Type 'left' or 'right'.  ").lower()

if choice1 == "right":
    print("You fell into a whole. Gave Over")
elif choice1 == 'left':
    choice2 = input("You come to a lake. Island in the middle of the lake. " \
    "Type 'wait' to wait for a boat. Type 'swim' to swim to the Island.  ").lower()
    if choice2 == "wait":
        choice3 = input("You have arrived to the Island now there are 3 doors. One 'red', One 'blue', One 'yellow'. Choose the door to get to the treasure.  ").lower()
        if choice3 == "red":
            print("Attacked by a Lion. Game Over")
        elif choice3 == "blue":
            print("Burned by fire. Game Over")
        elif choice3 == "yellow":
            print("You found the treasure. You Win!!")
        else:
            print("You chose the door that doesn't exist. Game Over")
    elif choice2 == "swim":
        print("You are attacked by a crocodile")
    else:
        print("You choice doesn't exist. Game Over")
else:
    print("You choice doesn't exist. Game Over")