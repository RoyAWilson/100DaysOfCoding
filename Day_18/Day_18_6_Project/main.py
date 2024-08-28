'''
create a painting in the style of Damien Hirst dot paintings
use colorgram to extract the colors used in a downloaded image.
Need to paint a painting with 10 x 10 grid of spots
dots should be around size 20 and spaced by around 50 steps.
Done without following the lecture.
'''

import random
import turtle
import colorgram

colours = colorgram.extract('2img.jpg', 25)
# print(colours)
# print(colours[0])

# Extract the RGB values:


def get_pallette(clrs: list):
    '''
    Extract colours as rgb tuples from list of colour tuples
    returns list of tuples rgb_colours
    '''
    rgb_colours = []

    for colouring in colours:
        r = colouring.rgb.r
        g = colouring.rgb.g
        b = colouring.rgb.b
        new_colour = (r, g, b)
        rgb_colours.append(new_colour)
    return rgb_colours


def get_rnd_colour(clr_plt) -> tuple:
    '''Grab a colour from a list
    and return clr, a tupple of RGB colour
    '''
    clr = random.choice(clr_plt)
    return clr


def draw_row() -> None:

    for _ in range(1, 11):
        tim.pendown()
        tim.dot(get_rnd_colour(pallette))
        tim.penup()
        tim.forward(50)


pallette = get_pallette(colours)

# print(pallette)

turtle.colormode(255)
screen = turtle.Screen()
tim = turtle.Turtle()

# Set starting position of the turtle.
tim.penup()
tim.setpos(-290, -270)
tim.pencolor(get_rnd_colour(pallette))
tim.pensize(20)
tim.hideturtle()
tim.speed('fastest')

# get rows drawn:

for _ in range(1, 11):
    tim_x = tim.pos()[0]
    tim_y = tim.pos()[1]
    draw_row()
    tim.setpos(-290, (tim_y + 60))

screen.exitonclick()
# print(tim.pencolor())


# Tutor created a list of colours and deleted several that she though were background colours then commented out the
# code to get and make a list of tuples of the colours.  Also didn't bother with positions, just turned the turtle
# and tracked it back to the start of next line.
# Did not define any functions.
