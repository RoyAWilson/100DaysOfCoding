from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
# tim.shape('square')
# tim.shapesize(stretch_len=20, stretch_wid=20)
tim.color('black')
tim.hideturtle()
tim.write('Help!', True, 'center', ('Arial', 20, 'normal'))
screen.exitonclick()
