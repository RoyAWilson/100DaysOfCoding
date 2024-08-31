'''
Set up the screen for a pong game
screen size 600h 800w
Screen should stay on screen till clicked.
Paddle width 20 height 100 xpos 350 ypos 0
'''

from turtle import Turtle, Screen
import time
from draw_paddle import Paddle
from ball import Ball

screen = Screen()
# Set up screen size, colour and title
screen.screensize(canvheight=600, canvwidth=800, bg='black')
screen.title('Pong')
# screen.tracer(0)

listener = screen.listen()
# Set up the paddles.
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
# move_right_paddle
screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')
screen.exitonclick()
ball.move()
print(ball.xcor(), ball.ycor())
game_on = True

while game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
