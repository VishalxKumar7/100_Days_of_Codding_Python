import random
import turtle as t

color = ["chartreuse", "peru", "navy", "firebrick", "dark magenta", "red", "medium purple", "dark green"]

tim = t.Turtle()

# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

#*********************************************************************************************

# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

#************************************************************************************************

# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range( num_sides):
#         tim.forward(100)
#         tim.right(angle)

# for shape_side_n in range(3, 11):
#     tim.color(random.choice(color))
#     draw_shape(shape_side_n)

#************************************************************************************************

# direction = [0, 90, 180, 270]
# tim.pensize(10)
# tim.speed(10)
# turtle.colormode(255)

# def random_color():
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)

#     random_color = (r, g, b)
#     return random_color


# for _ in range(300):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(direction))

# ***********************************************************************************************

tim.speed("fastest")
t.colormode(255)
tim.hideturtle()

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    random_color = (r, g, b)
    return random_color


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(5)



screen = t.Screen()
screen.exitonclick()
