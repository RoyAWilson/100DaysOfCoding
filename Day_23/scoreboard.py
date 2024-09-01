'''
Class to print the score board to screen
'''

from turtle import Turtle

FONT = ("Times New Roman", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)

        self.shape('square')
        self.shapesize(stretch_len=3, stretch_wid=2)
        self.color('black')
        self.hideturtle()
        self.penup()
        self.setpos(-250, 250)
        self.prn_level = 0

    def write_level(self, level):
        self.write(f'Level: {level}', font=FONT)
        self.prn_level = level
        # Tutor incremented the level in a method of the class, didn't think to do that :()

    def game_over(self):
        self.setpos(0, 0)
        self.write(f'Game Over\nRoad Kill at level {
                   self.prn_level}', font=FONT, align='center')
