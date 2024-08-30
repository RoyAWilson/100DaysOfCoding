'''
To draw and control movement of food.
Inherits from Snake class
'''

from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=.5, stretch_wid=.5)
        self.color('blue')
        self.speed('fastest')
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
        self.refresh()

    def refresh(self):
        '''
        Create new random position for the food.
        '''
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
