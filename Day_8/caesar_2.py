'''
Day 8 of 100 days challenge.
The Caesar Cypher
Tutor's solutioin to the challenge, which I cannot get to work correctly
'''

# Alphabets for cyphering:
# As per tutor's invitation am going to add capitals to the alphabet list as not having them seems very odd
# they would break the encryption algorithm as it stands.

Alphabet: list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                  'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                  'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ''
    shifted_position = 0

    if encode_or_decode == 'decode':
        shift_amount *= -1

    for letter in original_text:
        if letter not in Alphabet:
            output_text += letter
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
# Deals with this in the next lecture.  Have already done this in my working code in main.py so won't bother
# as this code is not working for me.
# Tutor addresses the problem with decoding throwing out unexpected letters late in chapter too
# Puts the test above the for loop which is the obvious place for it.  This makes it work but tutor should
# have told us ahead of time that she was building in a debug excercise, spent ages retyping code in case of error
# and trying to think through why the code would work as is!
