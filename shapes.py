# from random import random
# from turtle import Turtle, Screen
import turtle as t
import random

tim = t.Turtle()
tim.shape("turtle")
tim.color("red")
tim.pensize(10)

colors = ["red", "green", "blue", "orange", "violet", "indigo", "purple", "grey", "magenta"]

def draw_shape(number_of_sides):
    angle = 360 / number_of_sides

    for _ in range(number_of_sides):
        tim.forward(100)
        tim.right(angle)

for shape_side_n in range(3, 20):
    tim.pos()
    tim.color(random.choice(colors))
    draw_shape(shape_side_n)



# square = t.Turtle()
# pentagon= t.Turtle()
# hexagon = t.Turtle()
# octagon = t.Turtle()
# nonagon = t.Turtle()
# decagon = t.Turtle()
#
#
# for _ in range(1):
#     triangle.forward(100)
#     triangle.right(120)
#     triangle.forward(100)
#     triangle.right(120)
#     triangle.forward(100)













screen = t.Screen()
screen.exitonclick()
