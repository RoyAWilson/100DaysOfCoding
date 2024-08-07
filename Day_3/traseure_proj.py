'''
Very simple text game to find the treasure.
'''

print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')

print('Choose the direction to go and find the treasure!')

direction = input(
    'Which direction do you want to set off in? (Right/Left) ').upper()
if direction == 'RIGHT':
    print('You are abducted by alienss and die from space flu. RIP Adventurer have a nice afterlife.')
elif direction == 'UP' or direction == 'DOWN' or direction == 'EAST' or direction == 'WEST' or direction == 'NORTH' or direction == 'SOUTH':
    print('Please only enter Left or Right! There will be not further warnings!')
elif direction == 'LEFT':
    print('You have arrived at bay on a large cold lake bounded by cliffs')
else:
    print('YOU WERE WARNED.  YOUR LIFE FORCE HAS BEEN SUCKED OUT OF YOU BY RABID VAMPIRES! YOU LOSE!')
transport = input(
    'Will you swim the lake or will you wait for the ferry to get across? (Wait/Swim)').upper()
if transport == 'SWIM':
    print('You have angered the kraken, who drags you to the bottom and drons you! RIP')
elif transport != 'WAIT':
    print('Any adventurer who can\'t follow simple instructions will be killed with extreme malice.  RIP!')
else:
    door = input('The ferryman brings you safely to the other bank, where there are 3 buildings.  Will you take the left, right or centre door? (Left/Right/Centre)').upper()
    if door == 'LEFT':
        print('You step through the dark doorway and drop 100 feet to your death on vicioius spikes.  RIP.')
    elif door == 'CENTRE':
        print('You are transported to the surface of Beetlejuice where you die a horrible death. RIP')
    elif door == 'RIGHT':
        print('You enter a large room filled with treasure of every kind and return home a wealthy person!')
    else:
        print(f'Door {door} is not a choice, in trying to find door {
              door} you run into a cannibal tribe and they eat your brains.  RIP')

print('Game Over!')
# Tutor's solution a little different to mine but both work the same.
