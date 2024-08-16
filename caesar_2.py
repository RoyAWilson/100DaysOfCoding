'''
Day 8 of 100 days challenge.
The Caesar Cypher
Tutor's solutioin to the challenge, which I cannot get to work correctly
'''

# Alphabets for cyphering:

Alphabet: list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                  'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ''
    shifted_position = 0

    for letter in original_text:
        if encode_or_decode == 'decode':
            shift_amount *= -1
        shifted_position = Alphabet.index(letter) + shift_amount
        shifted_position %= len(Alphabet)
        output_text += Alphabet[shifted_position]
    print(f'Here is the encoded result:  {output_text}')


text = input('Enter the text to encrypt or decrypt > ')
shift_by = int(input('What offset? > '))
direction = input('Would you like to encode or decode? > ')

caesar(text, shift_by, direction)

# Cannot get this to work as the tutor's does.  Encode seems fine but decode will not work properly.

# By multiplying by -1 you are counting back by shifted amount items - might explain why decrypt is not working as expected on words
# longer than 1 letter.

# Don't like that it doesn't respect case not that it fails with muktiple word entries and has no way of
# dealing with punctation.
