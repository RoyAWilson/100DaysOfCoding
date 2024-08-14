'''
Create a function with multiple inputs
'''


def greet_with(name, location) -> str:
    '''
    To greet someone and ask if they
    are enjoying their visit to a
    location
    '''

    return f'Hello, {name}, are you enjoying your visit to {location}?'


name = input('Please enter your name >')
location = input('Please enter the location you are visiting > ')

# First with positional arguments:

print(f'{greet_with('Roy', 'London')}')

# OR with keyword arguments:

print(f'{greet_with(location='London', name='Roy')}')
