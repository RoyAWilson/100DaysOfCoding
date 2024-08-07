'''
revisit the bmi program to add message underweight, normal weight or overweight
'''

weight = 85
height = 1.85

bmi = weight / (height ** 2)

if bmi >= 25:
    print('Overweight')
elif bmi > 18.5:
    print('Normal weight')
else:
    print('Underweight')
