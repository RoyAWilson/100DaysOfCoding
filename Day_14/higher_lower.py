'''
Guess higher or lower game
using instagram followers from the provided file,
have no idea how old the actual file is.
concept - given two instagram accounts, guess which has more followers.
Game continues till you get the higher or lower wrong.
in game_data.data dictionary of insta people, with following keys:
Name = Name string
follower count = follower count int
description = description of reason for fame
country = country of origin.
'''

# import the necessary modules first.

from os import system
from random import randint
import art
import game_data

# print(len(game_data.data)) == 50 but can use len in the randomisation.
# escape sequences in art.py need fixing. Done

# First make sure playing on a cleared screen


system('cls')

# grab details of 2 of the records.:


def get_records_nos() -> tuple:
    '''
    Grab 2 random integers to get random records from the game data.
    '''

    rec_1 = randint(0, len(game_data.data)-1)
    rec_2 = randint(0, len(game_data.data)-1)
    while rec_1 == rec_2:
        rec_2 = randint(0, len(game_data.data))
    return rec_1, rec_2


def fetch_records(item) -> str:
    '''
    To return required fields from the record, call one for each of the comparitors.
    '''
    name: str = game_data.data[item]['name']
    desc: str = game_data.data[item]['description']
    nation: str = game_data.data[item]['country']
    person = f'{name}, the {desc}, from {nation}.'
    followers = game_data.data[item]['follower_count']
    return person, followers


# Set up variable to hold the score:
score: int = 0

# bring up game logo:
print(art.logo)
print('''\n\n******************************************************************\nThe object of the game is to guess whether of the 2 instagrammers,
does the first or second have a higher follower count\nThe figures are in millions.\n******************************************************************''')
ask = input('Shall we play? (y/n) > ')
if ask == 'n':
    exit()


# Grab the 2 records required.  should be part of the game logo should print on each screen but the object sting only once.

first = get_records_nos()
account_1 = fetch_records(first[0])
account_2 = fetch_records(first[1])
acc_1_folls = account_1[1]
acc_2_folls = account_2[1]
# set up screen for first guess:
system('cls')
print(art.logo)
print(f'Compare A:  {account_1[0]}\n')
print(art.vs)
print(f'\nAgainst B:  {account_2[0]}')
# And get the guess.
guess: str = input(
    '\nWho has the more followers? Type \'A\' or \'B\': > ').lower()
if guess == 'a' and acc_1_folls > acc_2_folls:
    score += 1
    print(f'You\'re right! Current score is {score}')
elif guess == 'b' and acc_2_folls > acc_1_folls:
    score += 1
    print(f'You\'re right! Current score is {score}')
elif acc_2_folls == acc_1_folls:
    score += 1
    print('Either choice would be correct, there is a dead heat')
else:
    print(f'Sorry that\'s wrong, final score {score}')
