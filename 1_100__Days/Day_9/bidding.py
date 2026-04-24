### BIDDING PROCESS

from art import logo
print(logo)

## MY CCODE
# bid = {}

# continue_bid = False

# while not continue_bid:
#     name = input("What is your name?: ")
#     amount = input("What's your bid?: ")

#     bid[name] = amount

#     other_bidder = input("Are there any other bidder? Type 'yes' or 'no': ").lower()
    
#     if  other_bidder == "no":
#         continue_bid = True

# print(max(bid))

# **********************************************************************************************
# COURCE CODE

bids = {}
continue_bidding = True

def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is  {winner} with a bid of ${highest_bid}")


while continue_bidding:
    name = input("What is your name?: ")
    price = int(input("What is Your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidder? Type 'yes' or 'no'. \n").lower()

    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue == "yes":
        print("\n"*20)


