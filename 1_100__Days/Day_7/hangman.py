import random
from hangman_words import word_list
from hangman_art import Stages, logo, lost, you_win

print(logo)
word_chosen = random.choice(word_list)

placeholder = ""
for i in range(len(word_chosen)):
    placeholder += "_"

print(placeholder)

game_over = False
correct_letter = []
lives = 6

while not game_over:

    print(f"*************************{lives}/6 LIVES LEFT************************")
    guess = input("Guess the letter: ").lower()

    if guess in correct_letter:
        print(f"You've already gussed! {guess}")

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



    if guess not in word_chosen:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        if lives == 0:
            game_over = True
            print(f"****************************IT WAS <{word_chosen}>****************************")
            print(lost)

    if "_" not in display:
        game_over = True
        print(you_win) 

    print(Stages[lives])