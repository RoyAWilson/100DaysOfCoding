'''
OOP Using modules intro
'''

from turtle import Turtle, Screen

timmy = Turtle()

# Object attributes.

my_screen = Screen()
timmy.shape('turtle')
timmy.color('CornflowerBlue')
print(my_screen.canvheight)

# Object methods:

timmy.forward(100)
my_screen.exitonclick()
