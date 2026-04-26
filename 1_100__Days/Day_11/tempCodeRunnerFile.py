while stand:
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
#     temp = player_blackjack + chose
#     if chose == 11 and temp >= 21:
#         computer.append(1)
#         computer_blackjack += 1
#     else:
#         computer.append(chose)
#         player_blackjack += chose


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
