''' 
Random Walk - from looking at the expected result shown looks like a simple
walk on a lattice, all turns seem to be 90 degrees and each step the same size.
'''

import random
from turtle import Turtle, Screen

# RNG = [x for x in range(1, 361)]
# print(RNG)


def walk(steps: int):
    '''
    Produce a random walk with the turtle, with randomised colours
    '''
    tim = Turtle()
    SCREEN = Screen()
    clr: str = ''
    TURN_DIRECTION = ['left', 'right']
    BACK_FORWARD = ['back', 'forward']
    COLOURS: list = ['red', 'yellow', 'green', 'blue', 'purple', 'orange', 'firebrick4',
                     'SlateBlue2', 'goldenrod', 'dark orchid', 'PeachPuff2', 'chartreuse2']
    for i in range(steps):
        clr = random.choice(COLOURS)
        tim.pencolor(clr)
        tim.pensize(5)
        tim.speed(10)
        t_dir = random.choice(TURN_DIRECTION)
        b_for = random.choice(BACK_FORWARD)
        if t_dir == 'left':
            tim.left(90)
            if b_for == 'forward':
                tim.forward(30)
            elif b_for == 'back':
                tim.back(30)
        elif t_dir == 'right':
            tim.right(90)
            if b_for == 'forward':
                tim.forward(30)
            elif b_for == 'back':
                tim.back(30)
    SCREEN.exitonclick()


n_steps = int(input('How many steps should the walk take? > '))
walk(n_steps)
