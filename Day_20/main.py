from turtle import Turtle, Screen
import time
from Snake import Snake

SCREEN = Screen()
SCREEN.setup(600, 600)
SCREEN.bgcolor('black')
SCREEN.title('My Snake Game')
SCREEN.tracer(0)

snake = Snake()
SCREEN.listen()
SCREEN.onkey(snake.up, 'Up')
SCREEN.onkey(snake.down, 'Down')
SCREEN.onkey(snake.left, 'Left')
SCREEN.onkey(snake.right, 'Right')

game_on = True
while game_on:
    SCREEN.update()
    time.sleep(0.1)
    snake.move()
