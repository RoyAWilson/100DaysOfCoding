from turtle import Screen
import time
from Snake import Snake
from food import Food
from score import Score

SCREEN = Screen()
SCREEN.setup(600, 600)
SCREEN.bgcolor('black')
SCREEN.title('My Snake Game')
SCREEN.tracer(0)

snake = Snake()
food = Food()
score = Score()
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

    # Dectect collision with food:
    if snake.HEAD.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.Write_Score(1)

    # Detect collision with wall:

    if snake.HEAD.xcor() > 280 or snake.HEAD.xcor() < -280 or snake.HEAD.ycor() > 280 or snake.HEAD.ycor() < -280:
        # game_on = False
        score.high_reset()
        snake.snake_reset()

    # Detect collision with tail:

    for segment in snake.segments[1:]:

        if segment == snake.HEAD:
            pass

        elif snake.HEAD.distance(segment) < 10:
            # game_on = False
            score.high_reset()
            snake.snake_reset()


SCREEN.exitonclick()
