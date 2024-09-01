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

scoreboard = Scoreboard()
level = 1
scoreboard.write_level(level=level)
car = CarManager()
# car_list.append(CarManager())

game_is_on = True
while game_is_on:
    scoreboard.write_level(level=level)
    time.sleep(0.1)
    screen.update()
    car.make_car()
    car.move_car()

    # Detect turtle squised!:
    for item in car_manager.all_cars:
        if item.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
    if player.crossed():
        player.pos_reset()
        car.speed_up()
        level += 1
        scoreboard.clear()


screen.exitonclick()
