from turtle import Turtle, Screen
# # joe = turtle.Turtle()
#
# tim = Turtle()
import heroes
import villains
print(heroes.gen())

import turtle as t

tim = t.Turtle()


tim.shape("turtle")
tim.color("red")

for _ in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()
    # for gap in range(10):
    #     tim.pendown()
    #     tim.forward(10)
    #     tim.penup()
    #     tim.forward(10)
    #     tim.pendown()
    #     tim.forward(10)
    # tim.pendown()
    # tim.forward(100)


screen = t.Screen()
screen.exitonclick()
