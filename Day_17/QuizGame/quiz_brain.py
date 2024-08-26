''''
Module to run the game
'''


class QuizBrain:

    '''
    To handle asking questions, obtaining answer as input and scoring the quiz
    '''

    def __init__(self, question_list: list) -> None:
        '''
        To grab the question lest and set up 
        question_number (the question currently being asked),
        question_ list - the list of questions to ask
        score - keep track of the score.
        '''

        self.question_list: list = question_list
        self.question_number: int = 0
        self.score: int = 0

    def next_question(self) -> None:
        '''
        To move on to the next question if one exists in the data_bank
        and call check answer to check if the answer is correct.
        '''
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f'Q. {self.question_number}: {
                            current_question.text} (True/False) ')
        self.check_answer(user_answer, current_question.answer)

    def still_has_questions(self) -> bool:
        '''
        To check if there are still questions to ask
        returns True or False to caller.
        '''
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer) -> bool:
        '''
        To determine if the answer given is or is not correct
        '''
        if user_answer.lower() == correct_answer.lower():
            print('You got it right!')
            self.score += 1
        else:
            print('That\'s wrong!')
        print(f'The correct answer was {correct_answer}')
        print(f'Your score is {self.score}/{self.question_number}\n\n')
