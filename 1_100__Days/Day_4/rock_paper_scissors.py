# Rock, Paper, and Scissors Game

rock ='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___))
'''

paper = ''' 
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = ''' 
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
print("Welcome to the game of Rock, Paper, and scissors")

player_choice = int(input("Chose '0' for rock, '1' for paper and '2' for scissor : \n"))
computer = random.randint(0,2)

# if player_choice == 0 and computer == 0:
#     print("You")
#     print(rock)
#     print("\n")
#     print("Computer")
#     print(rock)
#     print("Draw")
# elif player_choice == 1 and computer == 1:
#     print("You")
#     print(paper)
#     print("\n")
#     print("Computer")
#     print(paper)
#     print("Draw")
# elif player_choice == 2 and computer == 2:
#     print("You")
#     print(scissors)
#     print("\n")
#     print("Computer")
#     print(scissors)
#     print("Draw")
# elif player_choice == 0 and computer == 1:
#     print("You")
#     print(rock)
#     print("\n")
#     print("Computer")
#     print(paper)
#     print("Computer Winns!")
# elif player_choice == 0 and computer == 2:
#     print("You")
#     print(rock)
#     print("\n")
#     print("Computer")
#     print(scissors)
#     print("You Winns!")
# elif player_choice == 1 and computer == 0:
#     print("You")
#     print(paper)
#     print("\n")
#     print("Computer")
#     print(rock)
#     print("You Winns!")
# elif player_choice == 1 and computer == 2:
#     print("You")
#     print(paper)
#     print("\n")
#     print("Computer")
#     print(scissors)
#     print("Computer Winns!")
# elif player_choice == 2 and computer == 0:
#     print("You")
#     print(scissors)
#     print("\n")
#     print("Computer")
#     print(rock)
#     print("Computer Winns!")
# elif player_choice == 2 and computer == 1:
#     print("You")
#     print(scissors)
#     print("\n")
#     print("Computer")
#     print(paper)
#     print("You Winns!")
# else:
#     print("Wrong choice. You Lose!")


# OR
game_image = [rock, paper, scissors]
print(f"Player \n {game_image[player_choice]}")
print(f"Computer \n {game_image[computer]}")

if player_choice >= 3 or player_choice < 0:
    print("Wrong Choice. You Lose!")
elif player_choice == 0 and computer == 2:
    print("You Winn!")
elif computer > player_choice:
    print("You Lose!")
elif computer ==0 and player_choice == 2:
    print("Your Lose!")
elif player_choice > computer:
    print("You Win!")
elif computer == player_choice:
    print("It's a Draw")
else:
    print("Wrong Choice. You Lose!")