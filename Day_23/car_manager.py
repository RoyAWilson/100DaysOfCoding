'''
Class to create and draw cars to screen
'''

from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
all_cars = []


class CarManager():
    ''''
    Draw cars and set their coords, start them moving
    '''

    def __init__(self) -> None:
        '''
        Initialise the variables etc.
        '''

        self.car_speed = STARTING_MOVE_DISTANCE

    def make_car(self):
        car_chance = random.randint(0, 6)
        if car_chance == 1:
            new_car = Turtle('square')
            new_car.penup()
            new_car.shapesize(stretch_len=3, stretch_wid=1)
            # self.new_car.setheading(180)
            y_pos = random.randint(-250, 250)
            new_car.setpos(300, y_pos)
            new_car.color(random.choice(COLORS))
            all_cars.append(new_car)

    # def speed_up(self):
    #     self.car_speed += MOVE_INCREMENT

    def move_car(self):
        for car in all_cars:
            car.backward(self.car_speed)

    def speed_up(self):
        self.car_speed += MOVE_INCREMENT
