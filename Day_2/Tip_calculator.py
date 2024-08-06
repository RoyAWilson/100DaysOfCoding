'''
To calculate total bill including tip and split by number of persons
Should ask total bill, tip percentage 10, 12, or 15
Number of persons to split bill by
'''

# My attempt without watching the lectures:

# Print welcome message

print('Welcome to the tip calculator')

# Get inputs

bill = input('Please enter total amount of bill:  $')
covers = input('How many people to split with:  ')
covers = float(covers)
tip = input('Enter tip percantage, 10, 12, or 15:  ')

# Calculate the total for each diner inc tip:

bill = round(float(bill) + (float(bill)*(float(tip)/100)), 2)
# print(bill)
# Calculate total to pay:

bill = round(bill / float(covers), 2)
print(f'Each person should pay ${bill}')
