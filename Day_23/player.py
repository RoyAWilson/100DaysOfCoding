'''
Player class, to build a player and place it at the bottom of the screen
ready to start play
'''

from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    '''
    Build and set up a play at the bottom of the screen
    '''

    def __init__(self) -> None:
        '''
        initialise the class variables etc.
        '''
        super().__init__()

        self.color('green')
        self.shape('turtle')
        self.penup()
        self.setpos(STARTING_POSITION[0], STARTING_POSITION[1])
        self.setheading(90)
