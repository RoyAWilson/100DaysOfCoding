'''
More on Turtle Graphics
and challenge 1
'''

from turtle import Turtle, Screen

tim = Turtle()
tim.shape('turtle')
tim.color('purple')

# Challenge 1 draw a 100 by 100 square anywhere on the screen

tim.forward(100)
tim.right(90)
tim.forward(100)
tim.right(90)
tim.forward(100)
tim.right(90)
tim.forward(100)
tim.right(90)
tim.pen()

tim.left(90)
tim.pen({'pendown': False})
tim.forward(100)
tim.left(90)
tim.forward(350)
tim.right(180)

# Draw a dashed line each dash 10 paces, repeat 50 times
# Not clear if requirement is for 50 dashes and 50 spaces
# or if should be cumulative 25 dashes and 25 spaces.

tim.pen({'pendown': True})
for i in range(1, 51):
    tim.forward(10)
    if i % 2 != 0:
        tim.pen({'pendown': False})
    else:
        tim.pen({'pendown': True})

screen = Screen()
screen.exitonclick()
