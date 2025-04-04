import random
import turtle as t
from turtle import *
from screen import *

tim = t.Turtle()
t.colormode(255)
tim.shape("turtle")
tim.pensize(3)
tim.speed("fastest")
#
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r,g,b)
    return color

def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

choice = int(input("Size of gape? "))
draw_spirograph(choice)


screen = t.Screen()
screen.exitonclick()


