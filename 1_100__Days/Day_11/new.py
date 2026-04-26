import random
import os
from art import logo, ace, two, three, four, five, six, seven, eight, nine, ten

# --- CONFIGURATION ---

# Map numerical values to the art lists imported from art.py
# 10, J, Q, K all usually use the 'ten' art list in your setup
art_mapper = {
    11: ace, 2: two, 3: three, 4: four, 5: five, 
    6: six, 7: seven, 8: eight, 9: nine, 10: ten, 1: ace
}

# --- HELPER FUNCTIONS ---

def deal_card():
    """Returns a random card value from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    """Calculates the score and handles Blackjack (0) and Ace reduction."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0 # 0 represents Blackjack in this logic
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
        
    return sum(cards)

def print_hand(cards_list):
    # 1. Get the list of art for each card in the hand
    # This assumes art_mapper[val][0] is a LIST of lines
    hand_visuals = [art_mapper[val][0] for val in cards_list]

    # 2. Get the height of the card (how many lines)
    rows = len(hand_visuals[0])

    # 3. Print row by row
    for i in range(rows):
        combined_row = ""
        for visual in hand_visuals:
            combined_row += visual[i] + "  "
        print(combined_row)
        
def compare(u_score, c_score):
    """Determines the winner based on the scores."""
    if u_score == c_score:
        return "Draw! 🙃"
    elif c_score == 0:
        return "Lose, opponent has Blackjack! 😱"
    elif u_score == 0:
        return "Win with a Blackjack! 😎"
    elif u_score > 21:
        return "You went over. You lose! 😭"
    elif c_score > 21:
        return "Opponent went over. You win! 😁"
    elif u_score > c_score:
        return "You Win! 😃"
    else:
        return "You lose! 😤"

# --- MAIN GAME LOOP ---

def play_game():
    print(logo)
    
    user_cards = []
    computer_cards = []
    is_game_over = False

    # Deal initial hands
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        
        print(f"\nYOUR HAND (Score: {user_score if user_score != 0 else 21}):")
        print_hand(user_cards)
        
        print(f"\nCOMPUTER'S FIRST CARD:")
        # Pass a list containing only the first computer card
        print_hand([computer_cards[0]])

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("\nType 'y' to get another card, 'n' to pass: ").lower()
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # Computer's Turn (Dealer hits until at least 17)
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    # Final Reveal
    print("\n" + "="*40)
    print(f"YOUR FINAL HAND (Score: {user_score if user_score != 0 else 21})")
    print_hand(user_cards)
    print(f"\nCOMPUTER'S FINAL HAND (Score: {computer_score if computer_score != 0 else 21})")
    print_hand(computer_cards)
    print("="*40)
    
    print(compare(user_score, computer_score))

# --- APP START ---

while input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == 'y':
    # This clears the terminal screen for a fresh start (Windows: 'cls', Mac/Linux: 'clear')
    os.system('cls' if os.name == 'nt' else 'clear')
    play_game()