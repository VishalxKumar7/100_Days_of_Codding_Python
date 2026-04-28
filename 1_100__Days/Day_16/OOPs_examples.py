# # One way to import
# import turtle
# timmy = turtle.Turtle()

# Another Way to import
# from turtle import Turtle, Screen
# timmy = Turtle()    # Timmy is an object
# print(timmy)
# timmy.shape("turtle")
# timmy.color("green")

# timmy.forward(200)

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()


#### Pokemon
from prettytable import PrettyTable
table = PrettyTable()
print(table)

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"

print(table)