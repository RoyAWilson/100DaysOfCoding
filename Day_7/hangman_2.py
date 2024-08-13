'''
To implement a simple version of hangman game
'''

import random

words: list = ['aardvark', 'baboon', 'camel']

# Choose a random word

choice: int = random.randint(0, len(words)-1)
chosen_word = words[choice]

print(chosen_word)
print('_' * len(chosen_word))

# Guess a letter and lower case it:


def guess():
    '''
    To get the player's guessed letter.
    and return as a string
    '''

    guessed_letter = input('Please guess a letter (a to z):  >').lower()
    # Add while loop to check that input is in face a letter and nothing else
    while guessed_letter not in 'abcdefghijklmnopqrstuvwxyz':
        print('Please enter letters only\n\n')
        guessed_letter = input('Please guess a letter (a to z):  >').lower()
    return guessed_letter


# make the below code blocks function/s
z: str = guess()
# set up the dashes
dashes: list = []
for i in range(0, len(chosen_word)):
    dashes.append('_')
prnt: str = ''
# Determine if guessed letter appears in the word:
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
    prnt += dashes[k]
# Print the letter and dashes, upper cased the letters to make it easier to read for the user.
print(prnt.upper())
