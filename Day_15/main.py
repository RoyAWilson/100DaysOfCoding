'''
Produce a virtual coffee machine, to make 3 flavours:
1. Espesso, 2. Latte, 3. Cappuccino
Recipes:
Espresso - 50ml water, 18g coffee; latte - 200ml water, 24g coffee, 150ml milk; cappuccino - 250ml water, 250g coffee, 100ml milk
prices - Espresso $1.50, Latte $2.50, cappuccino $3.00
Starting resources: 300ml water, 200ml milk, 100g coffee
Coin operated, denominations - penny 1c, nickel 5c, dime 10c, quarter 25c
Requirements: Machine be able to print report - how much water left, how much coffee left, how much milk left, and money collected.
To get report from machine type: "Report"
Check for sufficient resources when drink ordered
When user order, ask them to insert coins - done as how many quarters etc. expecting an integer.
Makes change and delivers an eg. latte/
subtracts used resources from the resources.
If user orders a coffee and there are not enough resources, print out that there is not enough water etc. to fulfill the order.
Add up the coins inserted and tell user if not enough money to cover the cost of the coffee and refunds money
If enough coins entered calculate change and let user know how much change given.
Should tell user to enjoy their drink.

'''
import decimal


def prnt_res(curr_resouces: dict) -> str:
    '''
    return string detailing resources currently available
    argument - dictionary with resources.
    '''
    curr_res = f'The resources currently available are\nWater:  {curr_resouces['water']},\nCoffee: {
        curr_resouces['coffee']},\nMilk: {curr_resouces['milk']},\nCash: {curr_resouces['cash']}'
    return curr_res

# 3 Get order


def get_order() -> str:
    '''
    Get the customr's order, returns string
    Continue asking for input till an order matches menu item - probably better to check against the menu dict.
    '''
    ordered = input(
        'Please enter your order from one of the following:\nEspresso ($1.50)\nLatte ($2.50)\nCappuccino ($3.00)\n> ').lower()
    while ordered != 'espresso' and ordered != 'latte' and ordered != 'cappuccino' and ordered != 'resources' and ordered != 'off':
        ordered = input(
            'Sorry, that option is not on the list.\nPlease enter either:\nEspresso ($1.50)\nLatte ($2.50)\nCappuccino ($3.00)\n> ').lower()
    return ordered

# Grab ingredients list for the order


def coffee_ingredients(cust_order: str) -> dict:
    '''
    argument order string returns a dictionary of ingredients to make the customer order
    '''
    ingredients_list: dict = MENU[cust_order]
    return ingredients_list

# Check resources sufficient to make the drink order


def res_check(coffee_needs: dict, resources_available: dict, order: str) -> bool:
    '''
    Check have enough ingredients to make the coffee
    coffee_needs dict
    '''
    can_make = True
    if order == 'latte' and coffee_needs['ingredients']['water'] > resources_available['water'] or coffee_needs['ingredients']['coffee'] > resources_available['coffee'] or coffee_needs['ingredients']['milk'] > resources_available['milk']:
        can_make = False
    elif order == 'cappuccino' and coffee_needs['ingredients']['water'] > resources_available['water'] or coffee_needs['ingredients']['coffee'] > resources_available['coffee'] or coffee_needs['ingredients']['milk'] > resources_available['milk']:
        can_make = False
    elif order == 'espresso' and coffee_needs['ingredients']['water'] > resources_available['water'] or coffee_needs['ingredients']['coffee'] > resources_available['coffee']:
        can_make = False

    return can_make

# 6. Feedback to customer what is missing to fullfil their order.


def missing_ing(resources_available: dict, order: str) -> str:
    '''
    Takes resourcs_available - dict, order str returns str of first missing ingredient
    '''
    missed = ''
    if MENU[order]['ingredients']['water'] > resources_available['water']:
        missed += 'Too little water'
    elif MENU[order]['ingredients']['coffee'] > resources_available['coffee']:
        missed += 'Too little coffee'
    elif MENU[order]['ingredients']['milk'] > resources_available['milk']:
        missed += 'Too little milk'
    return missed + ' your money will be refunded'


def calc_cost(order_made: str) -> float:
    '''
    Takes order_made as string, returns the cost as a float'''
    cost = MENU[order_made]['cost']
    return float(cost)

# 3. calculate current resources.


def calc_resources(order: str, res: dict, ingredients: dict) -> dict:
    '''
    Recalculate resources available after order
    Takes order - string
    res - dictionary
    ingredients dict
    Returns dict of updated resources.
    '''
    res['water'] = res['water'] - ingredients[order]['ingredients']['water']
    res['coffee'] = res['coffee'] - ingredients[order]['ingredients']['coffee']
    res['milk'] = res['milk'] - ingredients[order]['ingredients']['milk']
    res['cash'] = res['cash'] + ingredients[order]['cost']

    return res


def payment(costs: float, money: dict, order: str) -> tuple:
    '''
    To get payment and ensure is enough to cover also make change.
    costs - float, money dict returns str
    '''
    pay_message = ''
    print(f'Please enter payment of ${costs} :\n')
    pennies = int(input('Number of pennies: > '))*money['Pennies']
    nickles = int(input('Number of nickles: > '))*money['Nickles']
    dimes = int(input('Number of dimes: > '))*money['Dimes']
    quarters = int(input('Number of quarters: > '))*money['Quarters']
    paid = pennies + nickles + dimes + quarters
    if paid < costs:
        pay_message = f'Sorry ${
            round(decimal.Decimal((paid)), 2)} is not enough to cover.  Your payment will be refunded.'
        trans_paid = False
    elif paid == costs:
        pay_message = f'Thank you.  Here is your {order}.  Enjoy!'
        trans_paid = True
    elif paid > costs:
        pay_message = f'Thank you.  Here is your {order}.  Enjoy!\nYour change of ${
            round(decimal.Decimal(paid - costs), 2)} will be returned.'
        trans_paid = True
    return pay_message, trans_paid


# would make life easier if menu showed espresso milk as needing 0 - decided to change to show milk 0
# as caused too many problems in availability checking function when not there.

MENU: dict = {
    'espresso': {
        'ingredients': {
            'water': 50,
            'coffee': 18,
            'milk': 0
        },
        'cost': 1.5
    },
    'latte': {
        'ingredients': {
            'water': 200,
            'coffee': 24,
            'milk': 158,
        },
        'cost': 2.5
    },
    'cappuccino': {
        'ingredients': {
            'water': 250,
            'coffee': 24,
            'milk': 100,
        },
        'cost': 3
    }
}

# 1. Set up initial resources for the coffee machine
RESOURCES: dict = {
    'water': 300,
    'coffee': 100,
    'milk': 200,
    'cash': 200,
}

CURRENCY: dict = {
    'Pennies': 0.01,
    'Nickles': 0.05,
    'Dimes': 0.1,
    'Quarters': 0.25,
}

# Get first input
start = True
while start is True:
    get_start = input('Do you want to order coffee y/n? > ')
    if get_start == 'n':
        exit()
    ordered = get_order()
    if ordered == 'resources':
        print(prnt_res(RESOURCES))
    elif ordered == 'off':
        exit()
    else:
        check_ingredients = coffee_ingredients(ordered)
        enough = res_check(check_ingredients, RESOURCES, ordered)
        if enough == False:
            missing = missing_ing(RESOURCES, ordered)
            print(missing)
        else:
            to_pay = calc_cost(ordered)
            pay = payment(to_pay, CURRENCY, ordered)
            print(pay[0])
            if pay[1] is True:
                RESOURCES = calc_resources(ordered, RESOURCES, MENU)
