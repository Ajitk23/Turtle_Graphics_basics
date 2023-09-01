import turtle as t 
import random

hurry = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b= random.randint(0, 255)
    random_colors = (r, g, b)
    return random_colors

directions = [0, 90, 180, 270]


for _ in range(200):
    hurry.pensize(20)
    hurry.color(random_color())
    hurry.speed("fastest")
    hurry.forward(30)
    hurry.setheading(random.choice(directions))