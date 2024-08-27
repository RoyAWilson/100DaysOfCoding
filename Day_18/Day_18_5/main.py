'''
Spirograph for making circles
'''

import random
import turtle


def random_colour() -> tuple:
    r: int = random.randint(0, 255)
    g: int = random.randint(0, 255)
    b: int = random.randint(0, 255)
    new_colour = (r, g, b)
    return new_colour


screen = turtle.Screen()
tim = turtle.Turtle()
turtle.colormode(255)
tim.setposition((0.00, 0.00))
tim.speed('fastest')
for i in range(1, 120):
    tim.color(random_colour())
    tim.circle(100)
    tim.right(3)


screen.exitonclick()

# Tutor uses get heading and set heading to move the second and subsequent circles by 5 degrees,
# seems like a lot of work just to change the heading slightly.
# also makes the drawing a function with number of repeats and divides it into 360 wrapped in int
# to enable the drawing to stop after n iterations.
# would only really need this if wanted to change the density of circles drawn, which was not part of the challenge.
