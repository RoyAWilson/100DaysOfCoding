'''
Scoreboard class for Pong
'''

from turtle import Turtle


class Scoreboard(Turtle):

    ''''
    Class to keep score of the gams
    '''

    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        '''
        To update the scoreboard with latest score.
        '''
        self.setpos(-100, 200)
        self.write(self.l_score, align='center',
                   font=('Times New Roman', 80, 'normal'))
        self.setpos(100, 200)
        self.write(self.r_score, align='center',
                   font=('Times New Roman', 80, 'normal'))

    def l_point(self):
        '''
        Add score to left player of 1 point
        '''
        self.clear()
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        '''
        Add to right player's score by 1 point
        '''
        self.clear()
        self.r_score += 1
        self.update_scoreboard()

    def game_over(self):
        '''
        To handle printing game over,
        only implemented for running out of coints.
        Added this to have a way to get to game over,
        this was missing from the challenge.
        '''
        self.setpos(0, 0)
        self.write('Game Over.\nYour coins ran out', align='center',
                   font=('Times New Roman', 20, 'bold'))
