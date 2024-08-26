'''
More with turtle
produce a drawing of a triangle, a square, a pentagon, hexigon, heptagon, octogon, nonogon
with line length 100 and with randomised colours.
'''

import random
from turtle import Turtle, Screen

tim = Turtle()
my_screen = Screen()
COLOURS: list = ['red', 'yellow', 'green', 'blue', 'purple', 'orange', 'firebrick4',
                 'SlateBlue2', 'goldenrod', 'dark orchid', 'PeachPuff2', 'chartreuse2']
# Triangle
for i in range(1, 4):
    tim.forward(100)
    clr = random.choice(COLOURS)
    tim.pencolor(clr)
    tim.right(360/3)
# Square
for i in range(1, 5):
    clr = random.choice(COLOURS)
    tim.pencolor(clr)
    tim.forward(100)
    tim.right(90)

# Pentagon
for i in range(1, 6):
    clr = random.choice(COLOURS)
    tim.pencolor(clr)
    tim.forward(100)
    tim.right(360/5)

# hexagon
for i in range(1, 7):
    clr = random.choice(COLOURS)
    tim.pencolor(clr)
    tim.forward(100)
    tim.right(360/6)

# heptagon
for i in range(1, 8):
    clr = random.choice(COLOURS)
    tim.pencolor(clr)
    tim.forward(100)
    tim.right(360/7)

# Octogon
for i in range(1, 9):
    clr = random.choice(COLOURS)
    tim.pencolor(clr)
    tim.forward(100)
    tim.right(360/8)

# Nonogon
for i in range(1, 10):
    clr = random.choice(COLOURS)
    tim.pencolor(clr)
    tim.forward(100)
    tim.right(360/9)

# Decagon

for i in range(1, 11):
    clr = random.choice(COLOURS)
    tim.pencolor(clr)
    tim.forward(100)
    tim.right(360/10)

my_screen.exitonclick()

# Tutor sets as a function with a number of sides variable and a variable that holdsd the angle.  Thought a bout doing it that way but seemed a bit
# over the for a one off like this.
