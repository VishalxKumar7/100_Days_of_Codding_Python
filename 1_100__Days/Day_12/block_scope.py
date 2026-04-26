game_level = 4
enemies = ["Skeleton", "Zombie", "Alien"]

# def create_enemy():

#     if game_level < 5:
#         new_enemy = enemies[0]
    
#     print(new_enemy)  # This code will work becase the rule does not apply to if-else or loop 
#                       # If the game level is grater than 5 then this will print noting because it if statement will never execute and new_enemy will not be created

# create_enemy()

def create_enemy():
    
    new_enemy = ""
    if game_level < 5:
        new_enemy = enemies[0]

    print(new_enemy)        # Now it knows that new_enemy exists but it's empty
