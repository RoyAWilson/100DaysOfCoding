'''
To implement a simple version of hangman game
'''

import random

words: list = ['aardvark', 'baboon', 'camel']

# Choose a rangom word

choice: int = random.randint(0, len(words)-1)
chosen_word = words[choice]

print(chosen_word)
print()

# Guess a letter and lower case it:


def guess():
    '''
    To get the player's guessed letter.
    and return as a string
    '''

    guessed_letter = input('Please guess a letter (a to z):  >').lower()
    return guessed_letter


# print(guess())
z: str = guess()
# set up the dashes
dashes: list = []
for i in range(0, len(chosen_word)):
    dashes.append('-')
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
print(prnt.upper())
