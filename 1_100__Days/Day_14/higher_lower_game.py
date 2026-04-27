from art import logo, vs
from data import famous_persons
import random

def format_data(account):
    """ Takes the account data into printable format."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(user_guess, a_follower, b_follower):
    """ Take a user's guess and the follower counts and returns if they got it right."""
    if a_follower > b_follower:
        return user_guess == "a"
    else:
        return user_guess == "b"

print(logo)
score = 0
game_continue = True


account_a = random.choice(famous_persons)
account_b = random.choice(famous_persons)

while game_continue:

    print("\n"*20)
    print(logo)

    account_a = account_b
    account_b = random.choice(famous_persons)

    if account_a == account_b:
        account_b = random.choice(famous_persons)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    guess = input("Who has more followers? Type 'A' or 'B'").lower()


    a_follower_account = account_a['insta_follower_count']
    b_follower_account = account_b['insta_follower_count']

    is_correct = check_answer(guess, a_follower_account, b_follower_account)

    if is_correct:
        score += 1
        print(f"You're right! Current score {score}")
    else:
        print(f"Sorry, that's Wrong!. Final score: {score}")
        game_continue = False