'''
To create a mail merge? from the given letter
and replace the [name] placeholder
with a given name in the names file,
saving each letter in ReadyToSend folder
'''

with open(r'./Letters/starting_letter.txt', 'r') as letter_text:
    text_list = letter_text.readlines()
    letter_text.close()
with open(r'./Names/invited_names.txt') as names:
    names_list = names.readlines()
    names.close()
for i in range(len(text_list)):
    if text_list[i] == 'Dear [name],\n':
        for names in names_list:
            text_list[i] = f'Dear {names.strip()},\n'
            # print(text_list)
            with open(f'./ReadyToSend/{names.strip()}.txt', 'w') as new_letters:
                new_letters.writelines(text_list)

# Done without watcing lecture.
