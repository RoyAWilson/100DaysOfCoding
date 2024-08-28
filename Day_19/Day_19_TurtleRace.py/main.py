'''
Build a turtle race
At start popup to bet on a colour of turtle that will win the race.  Inputs a colour.
After colour picked, line up 6 coloured turtles in starting position, ie far left of screen.
Then have them take random steps to right of screen, when completed print out
whether won or lost the bet.
'''

from random import randint
from turtle import Turtle, Screen

SCREEN = Screen()
SCREEN.setup(width=500, height=400)
COLOURS = ['red', 'yellow', 'orange', 'green', 'blue', 'purple']

# Set up turtles:


def set_up_turtle(colours) -> Turtle:

    name = Turtle(shape='turtle')
    name.penup()
    name.color(colours)
    return name

# Tutor didn't use a defined function for this.


y_pos = [-100, -60, -20, 20, 60, 100]
# Not keen on this way of setting y-pos, had aother way working calculating with a counter, but went with tutor's way.
turtle_list: list = []
for i in range(0, 6):
    new_turtle = set_up_turtle(colours=COLOURS[i])
    new_turtle.setposition(-233, y_pos[i])
    turtle_list.append(new_turtle)

# Bring up popup

user_bet = SCREEN.textinput(title='Make your bet!',
                            prompt='Which turtle will win the race,  enter a colour: ')

if user_bet:
    racing = True

while racing:
    for item in turtle_list:
        if item.xcor() > 230:
            racing = False
            winning_colour = (item.pencolor())
            if winning_colour == user_bet:
                print(f'You Won! Winning colour was {winning_colour}')
            else:
                print(f'You Lose! Winning colour was {winning_colour}')
        rand_dist = randint(0, 10)
        item.forward(rand_dist)


SCREEN.exitonclick()
