'''
Produce random integers.
'''

import random


# produce 10 random number between 1 and 10

for i in range(0, 10):
    print(f'{i}.  {random.randint(1, 10)}')

# Tutor just rand randint several times and printed the result.  No loop or f string.
