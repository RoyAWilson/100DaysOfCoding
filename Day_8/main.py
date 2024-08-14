'''
Day 8 of 100 days challenge. 
The Caesar Cypher
Did this one on Giles\' also
'''


# Grab input:


def message() -> str:
    '''
    grab the message to encode or decode
    message_inp str to hold the message
    and return to caller.
    '''
    message_inp: str = input('Please enter the message to encode > ')
    return message_inp
