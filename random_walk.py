import random
import turtle as t
tim = t.Turtle()
t.colormode(255)
tim.shape("turtle")
tim.pensize(15)
tim.speed("fastest")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r,g,b)
    return random_color


colors = ["red", "green", "blue", "orange", "violet", "indigo", "purple", "grey", "magenta"]
directions = [0, 90, 180, 270]

for _ in range(500):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))


