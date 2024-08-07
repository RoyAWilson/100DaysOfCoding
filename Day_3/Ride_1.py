'''
revisit the ride program and add another conditional - do you wnant a photo? Where yes add £3 to cost
'''

print('Welcome to the roller coaster!')

bill = 0

height = int(input('What is your height in centimetres? '))
if height >= 120:
    age = int(input('Please enter your age in years:  '))
    if age >= 18:
        bill = 10
        print('Your ticket Will be £10.')
    elif age > 12:
        bill = 7
        print('Your ticket Will be £7.')
    else:
        bill = 5
        print('Your ticket Will be £5.')
    photo = input(
        'Would you like a photo of your ride for an extra £3? y for yes n for no  ')
    if photo == 'y':
        bill += 3
        print(f'Your total ticket price with photo is £{bill}')
    else:
        print(f'Your total ticket price is £{bill}')

else:
    print('Sorry you are too short, minimum height is 120cm')

# Tutor started with <= 12 then <=18 ...
