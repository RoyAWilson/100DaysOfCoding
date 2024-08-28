'''
Intro to Event Listeners in Turtle
'''

from turtle import Turtle, Screen

tim = Turtle()
SCREEN = Screen()


def move_forwards() -> None:
    '''
    Move turtle forward by 10 paces, no parameters, returns None
    '''
    tim.forward(10)


SCREEN.listen()
SCREEN.onkey(key='space', fun=move_forwards)
SCREEN.exitonclick()
