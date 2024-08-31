'''
Class to draw and move the ball
'''

from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()

        self.color('white')
        self.shape('circle')
        self.penup()

    def move(self):
        # print(self.xcor(), self.ycor())
        new_x = self.xcor() + 10
        new_y = self.ycor() + 10
        self.setpos(new_x, new_y)
