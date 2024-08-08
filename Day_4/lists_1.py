'''
List of the states of the USA
'''

us_states: list = ['Washington', 'Montana', 'Idaho', 'Montana', 'North Dakota', 'South Dakota',
                   'Minasota', 'Wisconsin', 'Michigan', 'Maine', 'New Hampshire', 'Vermont', 'Massachusetts', 'New York',
                   'Road Island', 'Connecticut', 'New Jersey', 'Maryland', 'Delaware', 'Oregon', 'Wyoming', 'Nebraska', 'Iowa',
                   'Illinois', 'Indiana', 'Ohio', 'Pennsilvania', 'Maryland', 'California', 'Nevada', 'Utah', 'Colerado', 'Kansas', 'Missouri', 'Kentucky', 'West Virginia', 'Virginia', 'Arizona', 'New Mexico', 'Texas', 'Oklahoma', 'Arkansas',
                   'Louisiana', 'Tenessee', 'Mississippi', 'Alabama', 'Georgia', 'North Carolina', 'South Carolina', 'Georgia',
                   'Florida', 'Alaska', 'Hawaii']

# print(us_states)

# print(sorted(us_states))

# Slice find the Nth item:

print(us_states[0])
print(us_states[12])
print(us_states[-5])
print(us_states[4:12])

# Change an item:

us_states[2] = 'Fontana'
print(us_states[2])
us_states[2] = 'Montana'

# Add an entry to end of the list:

us_states.append('Disney Land')
print(us_states[-1])

# Extend - add more than 1 entry to the end:

us_states.extend(['Lalaland', 'Dollyland'])
print(us_states[-3:-1])

# Using insert:

us_states.insert(3, 'Bongoland')
print(us_states[3])
