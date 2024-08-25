from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# 1 Print current resources:

my_money_machine = MoneyMachine()
my_coffee_maker = CoffeeMaker()
my_menu = Menu()
is_on = True
# print(my_coffee_maker.report())
# print(my_money_machine.report())


while is_on:
    option = my_menu.get_items()
    user_choice = input(f'Which coffee would you like to order from the followeing {
                        option}? > ').lower()
    if user_choice == 'off':
        is_on = False
    elif user_choice == 'report':
        my_coffee_maker.report()
        my_money_machine.report()
    else:
        my_drink = my_menu.find_drink(user_choice)
        if my_coffee_maker.is_resource_sufficient(my_drink) and my_money_machine.make_payment(my_drink.cost):
            my_coffee_maker.make_coffee(my_drink)
