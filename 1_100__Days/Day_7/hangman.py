### HANGMAN GAME

# Importing necessary files
import random
from hangman_words import word_list
from hangman_art import Stages, logo, lost, you_win

# Printing the HANGMAN LOGO
print(logo)

# Chosing a random word
word_chosen = random.choice(word_list)

# Creating the intital placeholder that will show the how underscore for every word e.g:- "_______"
placeholder = ""
for i in range(len(word_chosen)):
    placeholder += "_"

print(placeholder)

# Creating variables and list
game_over = False
correct_letter = []
lives = 6

# Logic
while not game_over:

    print(f"*************************{lives}/6 LIVES LEFT************************")
    guess = input("Guess the letter: ").lower()

    # If you gussed the word twice this will execute
    if guess in correct_letter:
        print(f"You've already gussed! {guess}")

    # Checking the your guess word it exists in the chosen word
    display = ""
    for letter in word_chosen:
        if letter == guess:
            display += letter
            correct_letter.append(guess)
        elif letter in correct_letter:
            display += letter
        else:
            display += "_"

    print(display)


    # Every time you gussed the wrong letter you lose a life and when it hits 0 you will lose
    if guess not in word_chosen:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        if lives == 0:
            game_over = True
            print(f"****************************IT WAS <{word_chosen}>****************************")
            print(lost)

    # If you gussed every letter you will win
    if "_" not in display:
        game_over = True
        print(you_win) 

    print(Stages[lives])