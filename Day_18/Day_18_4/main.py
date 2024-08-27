'''
Random Walk 2
Using a tupple to set a
truly random colouor
'''

import random
import turtle
from turtle import Screen

tim = turtle.Turtle()
turtle.colormode(255)  # Change colour mode from 0-1 to 0 - 255


def random_colour() -> tuple:
    r: int = random.randint(0, 255)
    g: int = random.randint(0, 255)
    b: int = random.randint(0, 255)
    new_colour = (r, g, b)
    return new_colour


directions = [0, 90, 180, 270]
tim.pensize(5)
tim.speed('fastest')
for i in range(1, 201):
    tim.color(random_colour())
    tim.forward(30)
    tim.setheading(random.choice(directions))
Screen.exitonclick()
