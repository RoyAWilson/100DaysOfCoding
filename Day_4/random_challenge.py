'''
Write code to choose a reandom name from a list to pay the bill:
'''

import random

names: list = ['Alice', 'Bob', 'Charlie', 'David', 'Emanuel']

# Generate a random number
# print who will pay:
# print out 20 times to check that all names come up
# for i in range(1, 21):
#     pay = random.randint(0, 4)
#     print(names[pay])

# Print the chosen one:

pay: int = random.randint(0, 4)
print(f'Today\'s will will be paid by:  {names[pay]}')

# Or use random.choice:

print(f'The lucky payer today will be:  {random.choice(names)}')
