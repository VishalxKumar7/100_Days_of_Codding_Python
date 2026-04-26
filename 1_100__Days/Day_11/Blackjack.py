# BLACKJACK GAME

import random
from art import logo

# ****************************************MY Code***********************************


# print(logo)

# cards = [11,2,3,4,5,6,7,8,9,10,10,10]

# player = []
# computer = []

# stand = True

# for i in range(2):
#     player.append(random.choice(cards))
#     computer.append(random.choice(cards))

# print(f"Your Cards {player}")
# print(f"Computers first Card [{computer[0]}]")

# player_blackjack = 0
# computer_blackjack = 0

# for i in player:
#     player_blackjack += i
# for i in computer:
#     computer_blackjack += i

# if player_blackjack == 21 or computer_blackjack == 21:
#     if player_blackjack == 21 and computer_blackjack != 21:
#         print(f"You Wins! {player}")
#         stand = False
#     elif player_blackjack == 21 and computer_blackjack == 21:
#         print(f"It's a Draw player1: {player}, player2: {computer}")
#         stand = False
#     else:
#         print(f"Computer Winds [{computer}]")
#         stand = False

# while stand:
#     chose = 0
#     hit = input("Do you want to draw a card? Type 'y' for yes, 'n' for no :").lower()
#     if hit == 'y':
#         chose = random.choice(cards)
#         temp = player_blackjack + chose
#         if chose == 11 and temp >= 21:
#             player.append(1)
#             player_blackjack += 1
#         else:
#             player.append(chose)
#             player_blackjack += chose
#             print(player)
#     if player_blackjack >= 21:
#         stand = False
#     else:
#         player_stand = input(f"Do you want to stand? Type 'y' if yes else 'n': ").lower()

#         if player_stand == 'y':
#             stand = False

# while computer_blackjack <= 16:
#     chose = 0
#     chose = random.choice(cards)
#     temp = computer_blackjack + chose
#     if chose == 11 and temp >= 21:
#         computer.append(1)
#         computer_blackjack += 1
#     else:
#         computer.append(chose)
#         computer_blackjack += chose


# if player_blackjack > computer_blackjack:
#     if player_blackjack > 21:
#         print(f"Your Cards {player}   Total = {player_blackjack}")
#         print(f"Computers Card {computer}   Total = {computer_blackjack}")
#         print(f"Computer Win!")
#     else:
#         print(f"Your Cards {player}   Total = {player_blackjack}")
#         print(f"Computers Card {computer}   Total = {computer_blackjack}")
#         print(f"You Win!")

# elif player_blackjack < computer_blackjack:
#     if computer_blackjack > 21:
#         print(f"Your Cards {player}   Total = {player_blackjack}")
#         print(f"Computers Card {computer}   Total = {computer_blackjack}")
#         print(f"You Win!")
#     else:
#         print(f"Your Cards {player}   Total = {player_blackjack}")
#         print(f"Computers Card {computer}   Total = {computer_blackjack}")
#         print(f"Computer Win!")
# else:
#     print(f"Your Cards {player}   Total = {player_blackjack}")
#     print(f"Computers Card {computer}   Total = {computer_blackjack}")
#     print(f"Draw!") 


# *******************************************Cource Code*****************************************

def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw!"
    elif c_score == 0:
        return "Lose, opponent has Blackjack"
    elif u_score == 0:
        return "Win with a Blackjack"
    elif u_score > 21:
        return "You went over. You lose"
    elif c_score > 21:
        return "Oppnent went over. You win"
    elif u_score > c_score:
        return "You Win"
    else:
        return "You lose"
def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1

    is_game_over = False

    def deal_card ():
        # return a random card from the deck
        cards = [11,2,3,4,5,6,7,8,9,10,10,10]
        card = random.choice(cards)
        return card

    def calculate_score(cards):
        """Take a list of cards and return the score calculated from the cards"""
        if sum(cards) == 21 and len(cards) == 2:
            return 0
        
        if 11 in cards and sum(cards) > 21:
            cards.remove(11)
            cards.append(1)

        return sum(cards)

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input(f"Type 'y' to get another card, Type 'n' to pass: ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True


    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

print("\n"*50)
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    play_game()