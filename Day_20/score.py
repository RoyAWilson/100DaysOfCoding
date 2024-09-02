'''
Class to keep score.
'''

from turtle import Turtle

with open('h_score.txt', 'r') as file:
    old_h_score = file.read()
    old_h_score = int(old_h_score)
    file.close()
    print(old_h_score)


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.setposition(-200, 270)
        self.color('white')
        self.hideturtle()
        self.new_score = 0
        self.high_score = old_h_score
        self.Write_Score(scored=1)

    def Write_Score(self, scored):
        '''
        Print the score to the screen
        '''
        self.clear()
        self.write(f'Score: {self.new_score} high score {self.high_score}', False,
                   'center', ('Times New Roman', 13, 'bold'))
        self.new_score += scored

    def high_reset(self):
        '''
        Record the highest score this game
        '''
        if self.new_score > self.high_score:
            self.high_score = self.new_score
            self.new_score = 0
            self.Write_Score(self.new_score)
            self.write_txt()

    def write_txt(self):
        with open('h_score.txt', 'w') as file:
            file.write(str(self.high_score))
            file.close()
            # Tutor added this to the high_score function but for me that caused an error
            # with the read buffer being unable to open.  Also useful to have the write code
            # as a seperate function so can be used for more than one player in future iterations.
    # def game_over(self):

    #     self.setposition(0, 0)
    #     self.write(f'Game Over', False,
    #                'center', ('Times New Roman', 20, 'bold'))
