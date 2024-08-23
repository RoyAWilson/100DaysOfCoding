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


# TODO 2. Print report of all current resouces.

# TODO 3. calculate current resources.
# TODO 4. grab payment and calculate any change required.
# TODO 5. update resources including adding payment to said resources.
# TODO 6. Feedback to customer what is missing to fullfil their order.

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
    while ordered != 'espresso' and ordered != 'latte' and ordered != 'cappuccino':
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


def res_check(coffee_needs, resources_available, order) -> str:
    '''
    Check have enough ingredients to make the coffee
    '''
    can_make = True
    if order == 'latte' and coffee_needs['ingredients']['water'] > resources_available['water'] or coffee_needs['ingredients']['coffee'] > resources_available['coffee'] or coffee_needs['ingredients']['milk'] > resources_available['milk']:
        can_make = False
    elif order == 'cappuccino' and coffee_needs['ingredients']['water'] > resources_available['water'] or coffee_needs['ingredients']['coffee'] > resources_available['coffee'] or coffee_needs['ingredients']['milk'] > resources_available['milk']:
        can_make = False
    elif order == 'espresso' and coffee_needs['ingredients']['water'] > resources_available['water'] or coffee_needs['ingredients']['coffee'] > resources_available['coffee']:
        can_make = False
    return can_make


def calc_cost(order_made: str) -> float:
    '''
    Rakes order_made as string, returns the cost as a float'''
    cost = MENU[order_made]['cost']
    return float(cost)

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
    'cash': 0,
}

CURRENCY: dict = {
    'Pennies': 0.01,
    'Nickels': 0.05,
    'Dimes': 0.1,
    'Quarters': 0.5,
}


# Test out functions as write them
order_string = get_order()
print(order_string)
coffee_ing = coffee_ingredients(order_string)
print(coffee_ing)
poss = res_check(coffee_ing, RESOURCES, order_string)
print(RESOURCES)
print(poss)
price = calc_cost(order_string)
print(price)
