'''
Day 8 of 100 days challenge.
The Caesar Cypher
Did this one on Giles\' also
'''

# Alphabets for cyphering:

Alpha_lower: list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                     'l', 'm', 'n', 'o', 'p', 'q', 'r', 's' 't', 'u', 'v', 'w', 'x', 'y', 'z']
Alpha_upper: list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                     'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# Punction and special chars in case they need encryping at some future point

Punctuation: list = [',', '.', '?', '@' '#', ' ', '!', '\'', '"', ';',
                     ':', '[', ']', '{', '}', '(', ')', '-', '£', '$', '%', '^', '&', '*']

# Grab input:


def message() -> str:
    '''
    grab the message to encode or decode
    message_inp str to hold the message
    and return to caller.

    Should this be all lower, all upper, or should it encrypt respecting case?  Tutor does not say
    '''
    message_inp: str = input('Please enter the message > ')
    return message_inp


def get_shift():
    '''
    To obtain offset to encode by
    returns integer
    sft: int variable to hold the number entered by user
    '''

    sft = input(
        'What offset would you like? Enter a number (best results with nus between 1 and 13) > ')
    return int(sft)


def encrypt(msg, shft_by) -> str:
    '''
    Encode the given message string using a basic caesar cypher
    encd: str being a string to hold the encoded output
    pos_in_alpha: int being holds position of character in list and changes to hold new position once calculated.
    msg: txt to pass the message as given
    shft_by: int to hold the given number of characters to shift by
    At end of alphabet wrap back to a or A.
    '''
    encd: str = ''
    pos_in_alpha: int = 0
    for char in msg:
        if char in Alpha_lower:
            pos_in_alpha = Alpha_lower.index(char)
            if pos_in_alpha + shft_by > 25:
                pos_in_alpha = pos_in_alpha + shft_by - 25
                encd += Alpha_lower[pos_in_alpha]
            elif pos_in_alpha + shft_by < 25:
                pos_in_alpha += shft_by
                encd += Alpha_lower[pos_in_alpha]
        elif char in Alpha_upper:
            pos_in_alpha = Alpha_upper.index(char)
            if pos_in_alpha + shft_by > 25:
                pos_in_alpha = pos_in_alpha + shft_by - 25
                encd += Alpha_upper[pos_in_alpha]
            elif pos_in_alpha + shft_by < 26:
                pos_in_alpha += shft_by
                encd += Alpha_upper[pos_in_alpha]

        # If necessary enter code here to shift numerals and other characteers.
        else:
            encd += char

    return encd


# x = 'Hello World!'
# y = 5
# z = encrypt(x, y)
# print(z)

to_enc = message()
shift = get_shift()
new_msg = encrypt(to_enc, shift)

print('Your encrypted message reads:\n\n')
print('*' * (len(new_msg)+4))
print(f'* {new_msg} *')
print('*' * (len(new_msg)+4))
