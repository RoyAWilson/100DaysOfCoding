'''
To check if an input integer is odd or even
'''

print('Check if number is odd or even')

num = int(input('Please type a number to check if it is odd or even:  '))

if num % 2 != 0:
    print(f'The number {num} is odd')
else:
    print(f'The number {num} is even')
