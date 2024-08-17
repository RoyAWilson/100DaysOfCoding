'''
Project to build a calculator program
ask for a number, ask to pick a sign + - * /
ask for second number
print the formula and calculated answer
Press y to continue calculation or n to star new calculation.

Immediately see a problem, there is no way to end the program - will need a stop all choice.

Tutor decided to use a recursive function instead of having a function for first run and anothe
for next.

Never did  address the problem of no way out of the loop!

'''


def subtract(brought_forward='', n1=0, n2=0) -> float:
    '''
    to subtract 2 numbers.
    brought_forward - number brought in from previous calculation else blank,
    n1 number to subtract from (set to brought forward if supplied)
    n2 number to subtract from n1
    '''

    if brought_forward == '':
        return n1-n2
    else:
        return float(brought_forward) - n2


def multiply(brought_forward='', n1=0, n2=0) -> float:
    '''
    to multiply 2 numbers.
    brought_forward - number brought in from previous calculation else blank,
    n1 number to multiply to (set to brought forward if supplied)
    n2 number to multiply by n1
    '''

    if brought_forward == '':
        return n1*n2
    else:
        return float(brought_forward) * n2


def division(brought_forward='', n1=0, n2=0) -> float:
    '''
    to divide 2 numbers.
    brought_forward - number brought in from previous calculation else blank,
    n1 number to divide into (set to brought forward if supplied)
    n2 number to divide by n1
    '''

    if n2 == 0:
        exit()
    if brought_forward == '':
        return n1 / n2
    else:
        return float(brought_forward) / n2


def addition(brought_forward='', n1=0, n2=0) -> float:
    '''
    to add 2 numbers.
    brought_forward - number brought in from previous calculation else blank,
    n1 number to add to (set to brought forward if supplied)
    n2 number to add to n1
    '''

    if brought_forward == '':
        return n1 + n2
    else:
        return float(brought_forward) + n2


calc_dict = {
    '+': addition,
    '-': subtract,
    '/': division,
    '*': multiply,
}
# print(calc_dict)

# Now try to multiply 4 by 4 using the dictionary using the keys

# Test function muliply with 2 numbers entered, and with a take forward filling out the brought forward.
# take_forward = '3'

# result = calc_dict['*'](take_forward, 4)
# print(result)

# build functionality:


def first_run() -> float:
    '''
    Grab inputs for operation functions
    no_1 float
    no_2 float
    op = calculation operation to use
    '''
    no_1 = float(input('Please entre the first number:  > '))
    no_2 = float(input('Please enter the second number:  > '))
    op = input('Please enter the operator to use\n+\n-\n*\n/\n\n')
    carried_forward = ''
    # Calculate first aggregate:
    results = calc_dict[op](brought_forward=carried_forward, n1=no_1, n2=no_2)
    return results


print('Welcome to the Calculator App\n\n')
print('Please provide the follwing inputs:\n\n')

# get first result:

result = first_run()
print(f'{result}\n\n')

# subsequent runs:

Cont = True
while Cont is True:
    next_calc = input(
        'Do you wish to continue calculation \'y\' or start new calculation \'n\' anything else Exits! > ')
    if next_calc == 'n':
        result = first_run()
        print(result)
    elif next_calc == 'y':
        no_2 = float(input('Please enter the next number:  > '))
        op = input('Please enter the operator to use\n+\n-\n*\n/\n\n')
        result = calc_dict[op](result, 0, no_2)
        print(result)

    else:
        print('Thanks for using me!')
        exit()
