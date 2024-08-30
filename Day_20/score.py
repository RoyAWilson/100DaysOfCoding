'''
Class to keep score.
'''

from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.setposition(0, 280)
        self.color('white')
        self.hideturtle()
        self.new_score = 0
        self.Write_Score(scored=1)

    def Write_Score(self, scored):
        '''
        Print the score to the screen
        '''
        self.clear()
        self.write(f'Score: {self.new_score}', False,
                   'center', ('Times New Roman', 13, 'bold'))
        self.new_score += scored

    def game_over(self):

        self.setposition(0, 0)
        self.write(f'Game Over', False,
                   'center', ('Times New Roman', 20, 'bold'))
