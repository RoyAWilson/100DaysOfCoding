'''
Project:
Generate a password using N letters, N numbers and N symbols - N input by the user
'''

import random

# Set up the variables first:

alpha: str = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
digit: str = '0123456789'
symb: str = '!£$%^*#~@|()[]'

# Obtain user input:

print('Welcome to the password generator.\nTo get started, firstly answer the following questions\nplease only use numbers')

n_char = int(input('Please enter required password length:  > '))
n_alpha = int(input('Please enter number of letters required:  > '))
n_digit = int(input('Please enter number of digits required:  > '))
n_symb = int(input('Please enter number of special characters required:  > '))
print('\n\nThank you!')

# Check the number sum of entries adds up to the required characters:

if n_char != n_alpha + n_digit + n_symb:
    print('Sorry, something is wrong the number of characters is not the same as the individual characters required.')

# Simple way - do this sequentially:

# first letters:

cnt: int = 0
pw: str = ''
for i in range(0, n_alpha):
    cnt = random.randint(0, 51)
    pw += alpha[cnt]

# and digits:

cnt = 0
for j in range(0, n_digit):
    cnt = random.randint(0, 9)
    pw += digit[cnt]
# print(pw)
# print(len(pw))

# Special characters:

cnt = 0
for k in range(0, n_symb):
    cnt = random.randint(0, 13)
    pw += symb[cnt]
# print(pw)
# print(len(pw))

# Hard version - not sequential
# Take what I have already and jumble it up!

cnt = 0
pw_scr: str = ''
for i in range(0, n_char):
    cnt = random.randint(0, n_char-1)
    pw_scr += pw[cnt]
print(f'Your new password is:  {pw_scr}')
# print(len(pw_scr))

# I think this could be improved by using functions and allowing the user to discard the geneated
# password and re-running the logic to produce another.

# Tutor uses random.choice

# For difficult level tutor uses a list for the password and uses random.shuffle().  Probably better than my way of doing it.
