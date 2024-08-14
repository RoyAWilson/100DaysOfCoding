
def greet(name_1, name_2) -> str:
    '''
    Produce a func to print 3 lines of text
    '''

    greet_1 = f'Good Morning{name_1}\nHow is your son {
        name_2}\nI hope you are both well!'
    return greet_1


name_one: str = input('what is your name? >')
name_two: str = input('what is your son\'s name? >')

greeting = greet(name_one, name_two)
print(greeting)
