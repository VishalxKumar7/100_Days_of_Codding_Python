"""SCOPRE :- When the function is defined and we assign the variable inside the function,
it is not accessible by the anyone outside of the function Which is also called as "Local Variable"
But when we create a function out side of the function it is called as a "Global Variable" and,
it can be accessed by any one evey function and outside of the funtion 
"""

## 1st example
enemies = 1   # Global
def increase_enemies():
    enemies = 2     # Local
    print(f"enemies inside function: {enemies}")

increase_enemies()      # the enemies values that is printed is inside the fuction 
print(f"enemies outside function: {enemies}")   # Here the value is printed which is ooutside of the funtion

# def drink_portion():
#     potion_strength = 2
#     print(potion_strength)

# drink_portion()
#print(drink_strength) # Tis shows the error because it can't access the potion_strength this print it does not exist


# This is same for the functions too

player_health = 10

def game():
    def drink_potion():
        potion_strength = 2
        print(player_health)
    
    drink_potion()      # We can call it here

#drink_portion()     # This will show the error because it is inside a function and we can access it 
print(player_health)