'''
Set up the screen for a pong game
screen size 600h 800w
Screen should stay on screen till clicked.
Paddle width 20 height 100 xpos 350 ypos 0
No way to get to game over in the lectures.
'''

from turtle import Screen
import time
from draw_paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
scoreboard = Scoreboard()
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_on = True
counter = 0
while game_is_on:
    time.sleep(ball.move_rate)
    screen.update()
    ball.move()
    scoreboard
    # Detect if ball has hit top wall or bottom wall

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    ball.move()

    # dectect collision with right paddle.

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Started off with an or statement in first elif statement but from what tutor said that
    # need a way to check which side to award points to,
    # guess I could have figured it out, but don't
    # want to change the code too much from the tutors model.

    elif ball.xcor() > 390:
        ball.replace()
        scoreboard.l_point()
        # Added to have a way to hit game over when cummulative missed is > 20 hits.
        # Decided that as this was originally
        # a coin op game to count down to out of credit on the machine.
        # Could also add a game over if score goes over eg 7 on one side.
        counter += 1
        if counter > 20:
            game_is_on = False
            scoreboard.game_over()
    elif ball.xcor() < -390:
        scoreboard.r_point()
        ball.replace()
        counter += 1
        if counter > 20:
            game_is_on = False
            scoreboard.game_over()
screen.exitonclick()
