def generate_deck_art():
    suits = ['♠', '♥', '♦', '♣']
    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    
    for suit in suits:
        print(f"\n--- {suit} SUIT ---")
        # We process cards in rows of 5 so they fit on your screen
        for i in range(0, len(ranks), 5):
            chunk = ranks[i:i+5]
            cards_in_row = []
            
            for rank in chunk:
                space = "" if rank == "10" else " "
                cards_in_row.append([
                    " ┌─────────┐ ",
                    f" │{rank}{space}       │ ",
                    " │         │ ",
                    f" │    {suit}    │ ",
                    " │         │ ",
                    f" │       {space}{rank}│ ",
                    " └─────────┘ "
                ])
            
            # Print the 7 rows of the cards side-by-side
            for row in range(7):
                line = ""
                for card in cards_in_row:
                    line += card[row]
                print(line)

generate_deck_art()