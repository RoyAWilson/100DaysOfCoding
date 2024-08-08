'''
Produce random floats
'''

import random

for i in range(0, 9):
    print(f'{i}.  {random.random()}')

# and now multiply by 10 to obtain a number with fraction:

for j in range(0, 9):
    print(f'{j}.  {random.random()*10}')

# And with random.uniform:

for k in range(0, 9):
    print(f'{k}.  {random.uniform(1, 10)}')
