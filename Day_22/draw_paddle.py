'''
Class to set up a paddle to be drawn to the screen:
'''

from turtle import Turtle


class Paddle(Turtle):
    '''
    Produce a paddle taking pos a tuple of co-ords to set position'''

    def __init__(self, pos):
        super().__init__()

        self.color('white')
        self.shape('square')
        self.shapesize(stretch_len=1, stretch_wid=8)
        self.penup()
        self.setpos(pos)
        self.go_up
        self.go_down

    def go_up(self):

        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
