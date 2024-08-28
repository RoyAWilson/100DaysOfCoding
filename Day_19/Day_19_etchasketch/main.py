'''
Challenge:
Etchasketch with Turtle
Keys should function thus: W - Forwards
S - Backwards, A - Anticlockwise, D - clockwise, C - Ckear screen and recentre the turtle.
'''

from turtle import Turtle, Screen


def fwd() -> None:
    '''
    Turtle forward 10
    '''
    tim.forward(10)


def bck() -> None:
    '''
    Turtle backward 10
    '''
    tim.back(10)


def anti() -> None:
    '''
    Turn turtle left
    '''
    tim.left(5)


def clck() -> None:
    '''
    Turn turtle right
    '''
    tim.right(5)


def clrscrn() -> None:
    '''
    Clear screen and recentre the turtle
    '''
    SCREEN.reset()
    tim.home()
    # tried tim.clear at first but lost turtle with that so changed to reset.
    # tim.showturtle()


tim = Turtle()
SCREEN = Screen()

SCREEN.listen()
SCREEN.onkey(key='w', fun=fwd)
SCREEN.onkey(key='s', fun=bck)
SCREEN.onkey(key='a', fun=anti)
SCREEN.onkey(key='d', fun=clck)
SCREEN.onkey(key='c', fun=clrscrn)

SCREEN.exitonclick()
