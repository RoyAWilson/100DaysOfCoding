'''
To open a file and read text from it
'''

text = open('file.txt', 'r')
file_cont = text.read()
print(file_cont)
text.close()

# Tutor didn't write to the file she opened the file
# from the file manager and edited it.
# Covers write method later in lecture.

append_text = '\nI am 59 years old.'
text = open('file.txt', 'a')
text.write(append_text)
text.close()
text = open('file.txt', 'r')
file_cont = text.read()
text.close()
print(file_cont)


# Also covers opening file in with statement

with open('file.txt', 'r') as text:
    file_cont = text.read()
    text.close()
    # apparently now using .close is not required.  I think I would still like to close the file manually just to be 100% sure
print(file_cont)

with open(r'../0_text_file/new_file.txt') as new_file:
    file_text = new_file.read()
    new_file.close()
print(file_text)

# Ooops tutor wanted us to use absolute referencing. She also used the desktop, but I don't want to do that.
# Tutor covers relative referencing further on in the lecture.
