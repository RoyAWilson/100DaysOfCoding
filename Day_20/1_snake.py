from turtle import Turtle, Screen
import time
'''
emulate the snake game that was packed with
the Nokia 3610.
Tutor sprung making this a class on us.  Now see why she had the start positions as a list.
Tried to get it working this way with the class, but ran into problems.  Realised too late
that I had missed the brackets round a tuple and that was the problem.
Had changed it to the same code the tutor used and too late in evening to 
change it back.

'''


def get_segments() -> Turtle:
    '''
    produce the first 3 tutles no inputs
    '''
    ttl = Turtle(shape='square')
    ttl.penup()
    ttl.color('white')
    return ttl


SCREEN = Screen()

SCREEN.bgcolor('black')
SCREEN.screensize(600, 600)
SCREEN.tracer(0)  # Turn off tracing to be able to control screen updates.

segments = 3
snake = []
pos = 0
segments_lst: list = []

for i in range(0, segments):
    segs = get_segments()
    snake.append(segs)
    snake[i].setposition(pos, 0)
    pos -= 20
    segments_lst.append(snake[i])

#  Get the snake to move

game_on = True

while game_on:
    SCREEN.update()
    time.sleep(0.1)
    for segnum in range(len(segments_lst)-1, 0, -1):
        new_x = segments_lst[segnum-1].xcor()
        new_y = segments_lst[segnum - 1].ycor()
        segments_lst[segnum].setposition(new_x, new_y)
    segments_lst[0].forward(20)

SCREEN.exitonclick()
