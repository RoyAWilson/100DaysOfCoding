'''
Today will be dictionaries and nesting - dictionaries in dictionaries, list in dictionaries etc.
'''

# Make a simple dictionary of programming keywords and a short description:
# Try before watching the lesson

my_dict = {
    'Bug': 'An error in a program that prevents it from runnign as expected',
    'Function': 'A piece of code that you can easily call over and over again',
    'Loop': 'An action doing something over and over again',
}
#  print(my_dict)

# Extract an item from the dictionary:

# print(my_dict['Loop'])

# Add a new key: value pair programmatically:

my_dict['Variable'] = 'A letter or word used to refer to a value'
print(my_dict)

# clear the dictionary entries:

# my_dict = {}
# print(my_dict)

# Edit item in dictionary

my_dict['Bug'] = 'A moth in your computer'
# print(my_dict)

# Looping through dictionary:

for key in my_dict:
    print(key)
    print(my_dict[key])
