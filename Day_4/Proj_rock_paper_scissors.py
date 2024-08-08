'''
Make a simple Rock, Paper, Scissors game
Tutor did it with input numbers not text and all conditionals were using < or > and =
Would probably be better as function and easier to follow.
'''

import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

choices: list = [rock, paper, scissors]

# print(choices[2])

# Start with welcome and user input:

# Choose computer's hand:

comp_choice: int = random.randint(0, 2)
comp_word: str = ''
if comp_choice == 0:
    comp_word = 'Rock'
elif comp_choice == 1:
    comp_word = 'Paper'
elif comp_choice == 2:
    comp_word = 'Scissors'
# print(comp_choice)
print('Welcome to Rock, paper, Scissors')
user_choice: str = input(
    'Please enter \'Rock\', \'Paper\' oe \'Scissors\' ').lower()
if user_choice == 'rock':
    k = 0
elif user_choice == 'paper':
    k = 1
elif user_choice == 'scissors':
    k = 2

print(f'You chose {user_choice}:\n\n{choices[k]}\n\n')
print(f'The computer chose {comp_word}\n\n{choices[comp_choice]}')

# Decide who wins:

if comp_choice == 0 and k == 0:
    print('Results:  DRAW')
elif comp_choice == 0 and k == 1:
    print('Result:  YOU WIN!')
elif comp_choice == 0 and k == 2:
    print('Result:  COMPUTER WINS!')
elif comp_choice == 1 and k == 0:
    print('Result:  COMPUTER WINS!')
elif comp_choice == 1 and k == 1:
    print('Result:  DRAW')
elif comp_choice == 1 and k == 2:
    print('Result:  YOU WIN!')
elif comp_choice == 2 and k == 0:
    print('Result: YOU WIN!')
elif comp_choice == 2 and k == 1:
    print('Result:  COMPUTER WINS!')
elif comp_choice == 2 and k == 2:
    print('Result:  DRAW')
else:
    print('Sorry something went wrong!')
