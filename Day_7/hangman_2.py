'''
To implement a simple version of hangman game
'''

import random

words: list = ['aardvark', 'baboon', 'camel', 'lion', 'tiger',
               'hyena', 'giraffe', 'sloth', 'alligator', 'bear', 'racoon']

# Ascii Art:

pix = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''',
       '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========''']

# Choose a random word

choice: int = random.randint(0, len(words)-1)
chosen_word = words[choice]

# print(chosen_word)
print('_' * len(chosen_word))

# Guess a letter and lower case it:


def guess():
    '''
    To get the player's guessed letter.
    and return as a string
    '''

    guessed_letter = input('Please guess a letter (a to z):  >').lower()
    # Add while loop to check that input is in face a letter and nothing else
    if guessed_letter == chosen_word:
        print('**********************************************************************************')
        print(f'Congratulation! You have guessed that the word was {
              chosen_word.upper()}!')
        print('**********************************************************************************')
        exit()
    elif len(guessed_letter) > 1 and guessed_letter != chosen_word:
        print(f'Sorry, {guessed_letter} is not the correct word')
        return guessed_letter
    else:
        while guessed_letter not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter letters only\n\n')
            guessed_letter = input(
                'Please guess a letter (a to z):  >').lower()
        return guessed_letter

# set up the dashes


def place_holder():
    '''
    Build the dasshes
    '''
    dash: list = []
    for i in range(0, len(chosen_word)):
        dash.append('_')
    return dash


dashes: list = place_holder()
# word: str = ''

# make the below code blocks function/s
# Determine if guessed letter appears in the word:


def determine():
    '''Determine whether letter in word if so add it, if not retain the dash
    '''
    word: str = ''
    if z in chosen_word:
        print('Congratulations, you have found a letter in the word!')
        # add letter to the dashes list:
        for j in range(0, len(chosen_word)):
            if chosen_word[j] == z:
                dashes[j] = z

    else:
        print('Sorry, that letter is not in the word!')

    # Make the list a string:
    for k in range(0, len(chosen_word)):
        word += dashes[k]
    return word


# Print the letter and dashes, upper cased the letters to make it easier to read for the user.
z: str = guess()
prnt = determine()
print(prnt.upper())

pic_count: int = 0
while prnt != chosen_word and pic_count <= 5:
    print(pix[pic_count])
    z: str = guess()
    prnt = determine()
    print(pix[pic_count])
    print(prnt.upper())
    if prnt == chosen_word:
        print('**********************************************************************************')
        print(f'Congratulation! You have guessed that the word was {
            chosen_word.upper()}!')
        print('**********************************************************************************')
    elif z not in chosen_word:
        pic_count += 1
        print('*******************************************')
        print(f'* You have {6 - pic_count} lives left! Use them wisely! *')
        print('*******************************************')
if pic_count >= 6:
    print(pix[6])
    print('*******************************************************')
    print(f'You Lose! The word was {chosen_word.upper()}')
    print('*******************************************************')

# Tutor also talks about importing the word list and the pictures rather than building them into the code
# However, the resources on Udemy seem to not have the required files.
