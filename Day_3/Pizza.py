'''
To work out the price of a pizza, choices small (S) £15, medium (M) £20 large (l) £25
Extras Peperoni (P) small £2, medium £3, large £3
Extra cheese to any size pizza £1
'''

price = 0

print('Welcome to the Python Pizzeria')

size = input('Please enter size required S(mall), M(edium), L(arge)').upper()
if size == 'S':
    price += 15
elif size == 'M':
    price += 20
else:
    price += 25
extras = input('would you like any extras? (Y/N)').upper()
if extras == 'N':
    print(f'Your total bill today will be £{price}')
if extras == 'Y':
    pepperoni = input('Extra pepperoni? (Y/N)').upper()
    if pepperoni == 'Y' and size == 'S':
        price += 2
    if pepperoni == 'Y' and size == 'M':
        price += 3
    if pepperoni == 'Y' and size == 'L':
        price += 3
    cheese = input('Would you like extra cheese? (Y/N)').upper()
    if cheese == 'Y':
        price += 1
print(f'Thank you for your order.  The total price of your pizza is £{price}')
# Turor didn't force case to allow for upper and lower.
