'''
Quiz game True False implemented with modules,
part 1 to work with data.py, then part 2
change the code to make it work with a download from https://opentdb.com/
Downloaded as a json but edited to form a py as
couldn't remember how to import json file learnt back in the
Linkedin course and didn't want to look it up at this point
as overkill for the rquirements of the project.
'''


from question_model import Question
from Data2 import question_data
from quiz_brain import QuizBrain

question_bank = []
more_questions = True

for question in question_data:
    question_text = question['question']
    question_answer = question['correct_answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)
    quiz = QuizBrain(question_bank)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f'That was the last question!\n\nYour final score was {
      quiz.score}/{quiz.question_number}')
