'''
revisit the ride.py file and add cost of £10 for 18 and over or £7 for under 18
then change else to elif and add over 12 under 18 pays £7 under 12 pays £5
'''

print('Welcome to the roller coaster!')

height = int(input('What is your height in centimetres? '))
if height >= 120:
    age = int(input('Please enter your age in yuears:  '))
    if age >= 18:
        print('Please pay £10 for your ticket and enjoy the ride!')
    elif age > 12:
        print('Please pay £7 for your ticket and enjoy the ride!')
    else:
        print('Please pay £5 for your ticket and enjoy your ride!')
else:
    print('Sorry you are too short, minimum height is 120cm')

# Tutor started with <= 12 then <=18 ...
