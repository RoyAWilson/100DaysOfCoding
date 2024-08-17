'''
More on Fucntions
and functions with outputs on day 10'''

# Challenge: create a function to take first and surname and return in title case:


def format_name(f_name, l_name) -> str:
    '''
    Return a string containing
    correctly capitalised name
    '''
    f_name = f_name.title()
    l_name = l_name.title()
    return f'{f_name} {l_name}'


forename: str = input('Enter your first name:  > ')
surname: str = input('Enter your surname:  > ')

full_name = format_name(forename, surname)
print(full_name)
