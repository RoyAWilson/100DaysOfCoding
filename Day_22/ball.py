'''
Class to draw and move the ball
'''

from turtle import Turtle


class Ball(Turtle):
    '''
    draw and move the ball
    '''

    def __init__(self):
        super().__init__()

        self.color('white')
        self.shape('circle')
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_rate = 0.1

    def move(self):
        '''
        Move the ball across the screen at diagonal
        '''

        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.setpos(new_x, new_y)

    def bounce_y(self):
        '''
        Handle bouncing the ball in the y plane on contact with the upper,
        ower wall or either paddle
        '''
        self.y_move *= -1

    def bounce_x(self):
        '''
        Handle bouncing the ball in the x plane on contact with the upper,
        ower wall or either paddle
        '''

        self.x_move *= -1
        self.move_rate *= 0.9

    def replace(self):
        '''
        Return ball to center screen and start movement toward the
        winning opponent.  Changed this slightly from the tutor's version
        '''
        self.setpos(0, 0)
        self.move_rate = 0.1
        self.bounce_x()
