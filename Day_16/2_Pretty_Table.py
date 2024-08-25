
'''
More on packages.  Using prettytable to produce a table.
I think I would rather use pandas to produce a table and export it to another
application to display it.
'''
from prettytable import PrettyTable

table = PrettyTable()
table.add_column('Pokemon Name', ['Pikachoo',
                 'Squirtle', 'Charmnander'], align='r')
table.add_column('Type', ['Electric', 'Water', 'Fire'], align='r')

print(table)
table.align = 'l'
print(table)
