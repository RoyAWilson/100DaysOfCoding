'''
revisit ride to add anyone over 45 and under 56 rides free.
'''

print('Welcome to the roller coaster!')

height = int(input('What is your height in centimetres? '))
if height >= 120:
    age = int(input('Please enter your age in yuears:  '))
    if age >= 45 and age <= 56:
        print('Congratulations you get to ride for free! Enjoy you ride!')
    if age >= 18 and age < 45 or age > 56:
        print('Please pay £10 for your ticket and enjoy the ride!')
    elif age > 12 and age < 18:
        print('Please pay £7 for your ticket and enjoy the ride!')
    else:
        print('Please pay £5 for your ticket and enjoy your ride!')
else:
    print('Sorry you are too short, minimum height is 120cm')

# Tutor started with <= 12 then <=18 ...
