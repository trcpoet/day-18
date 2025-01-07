import random
import turtle as t
from turtle import *
from screen import *

tim = t.Turtle()
t.colormode(255)
tim.shape("turtle")
tim.pensize(5)
tim.speed("fastest")
#
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r,g,b)
    return color

for _ in range(100):
    tim.color(random_color())
    tim.circle(100)
    current_heading = tim.heading()
    tim.setheading(current_heading + 10)


screen = t.Screen()
screen.exitonclick()


