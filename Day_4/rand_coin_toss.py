'''
Challenge to create a program that produces a coin toss and prints heads of tails
depending on a random number
'''

import random

rdn_coin: int = 0

# I want to do 10 coin flips though this is not part of the challenge

for i in range(1, 11):
    a = random.randint(a=1, b=2)
    if a == 1:
        print(f'Toss {i}:  Heads')
    else:
        print(f'Toss {i}:  Tails')
