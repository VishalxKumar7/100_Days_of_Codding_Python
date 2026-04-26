### NUMBER GUESSING GAME

import random
def number_guessing_game():
    print("Welcome to number guessing game!")
    num = random.randint(1, 101)

    difficulty = input(f"Chose the defficulty. Type 'Easy' for easy and 'Hard' for hard: ").lower()
    if difficulty == "easy":
        lives = 10
    elif difficulty == "hard":
        lives = 5
    else:
        print(f"Invalid Option. Default to easy.")
        lives = 10

    print(f"I'm thiking number between 1 and 100")

    while lives != 0:
        print("\n")
        print(f"You have {lives} attempts")
        try:
            guess = int(input("Make a Guess: "))
        except ValueError:
            print("Please enter a valid number!")
            continue
        if guess > num:
            print(f"Your Guess '{guess}' is high!")
            lives -= 1
        elif guess == num:
            print(f"Your have Guessed the number '{guess}'. You Win!")
            break
        else:
            print(f"Your Guess '{guess} is low!")
            lives -= 1
        
        if lives == 0:
            print(f"You have {lives} Guesses. You Lost!")

        
        
continue_game = True

while continue_game != False:
    print("\n"*5)
    choice = input("Do you want to play the 'Number Guessing Game'. Type 'y' for yes and 'n' for no: ").lower()
    if choice == 'y':
        number_guessing_game()
    elif choice == 'n':
        continue_game = False
    else:    
        print("Wrong Choice!")