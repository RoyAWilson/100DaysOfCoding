'''
Number guessing game with 2 levels of dificulty
each next level having few attempts to guess correctly.
to learn about scope.

First print a welcome and tell user it is thinking of a number between
1 and 100.

Asks to choose a dificulty level - easy or hard

If hard give 5 attempts to guess the number

Asks for a guess input and tell user if higher or lower than guess and not the number I am thinking of
reprint number of attempts adjusted and so on

Easy level 10 attempts

Tell user when they have guessed correctly.

Use Ascii art for the header
'''

from os import system
import random
import num_art


def number() -> int:
    '''
    Produce a random integer range 1 - 100
    '''
    rnd_no = random.randint(1, 100)
    return rnd_no


def check_guess(num: int, hidden: int) -> str:
    '''
    Check if the guessed number
    is = > or < the random number'''

    if num == hidden:
        message = 'correct'
    elif num > hidden:
        message = 'high'
    elif num < hidden:
        message = 'low'
    return message


def play():
    system('cls')
    print(num_art.logo)
    print()
    print('*' * 60)
    print(f'Welcome to the guess the number game.\nYou will be asked to guess a number in the range 1 - 100')
    print('*' * 60)

    secret_no = number()

    level: str = input(
        '\n\nWould you like to play at Hard level 5 guesses, or Easy level 10 guesses? > ').lower()
    if level == 'h':
        counter = 5
    else:
        counter = 10
    while counter != 0:
        guess = int(input('Please enter your guess:  > '))
        ret: str = check_guess(num=guess, hidden=secret_no)
        if ret == 'correct':
            print(f'Amazing!! You guessed correctly I was thinking of {
                secret_no}.')
            if (input('\n\n\nThat was fun! Would you like to play this game with me again? (y or n) > ')) == 'y':
                play()
            else:
                exit()
        if ret == 'low':
            print(f'Your guess, {guess} is too low!\n\n You have {
                counter - 1} guesses left!')
        if ret == 'high':
            print(f'Your guess, {guess} is too high!\n\n You have {
                counter - 1} guesses left!')
        counter = counter - 1
    print(f'\n\nThe number I was thinking of was:  {secret_no}')
    if (input('\n\n\nThat was fun! Would you like to play this game with me again? (y or n) > ')) == 'y':
        play()
    else:
        exit()


play()
