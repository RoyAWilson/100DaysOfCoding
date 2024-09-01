'''
Main program for the 
turtle crossing game
'''

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
import car_manager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
screen.listen()
screen.onkeypress(player.move_player, 'Up')

# car = CarManager()
car = CarManager()
# car_list.append(CarManager())

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.make_car()
    car.move_car()

screen.exitonclick()
