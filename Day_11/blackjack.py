'''Capstone project:

Implement a simplified version of
the game of blackjack.
Cards will not be marked as dealt
nor will there be any statistical work
Suits will not be used.
Deck will not contain JKQ but will rather have
these cards represented by 3 10 values, so not
need for a dictionary, only a list.
From what the first hint was looks like the
ace will always be counted as 11, should n't be too
dificult to check if over 21 and hand contains 11
subtract 10 to count as a 1.
Did something very similar on the Giles course.
No inputs
'''

# First import the random modeule to randomize the deal:

import random

# TODO DEFINE PLAY FUNCTION(S)


def deal_hand(dck) -> tuple:
    '''
    To deal a hand to both the player and the bank
    argument - dck - the deck in play
    card - a list containing the cards in play
    player_hand - list to hold player's cards
    bank_hand - a list to hold bank's cards
    '''

    player_hand = []
    bank_hand = []
    for i in range(0, 2):
        player_hand.append(dck[random.randint(0, 12)])
        bank_hand.append(dck[random.randint(0, 12)])
    return player_hand, bank_hand


def in_play(plyr_hand, bnk_hnd, dck) -> tuple:
    '''
    To deal further cards if necessary
    arguments: plyr_hand LIST hand, bnk_stnd LIST, dck LIST

    '''
    plyr_hand.append(dck[random.randint(0, 12)])
    bnk_hnd.append(dck[random.randint(0, 12)])
    return plyr_hand, bnk_hnd


def stand(p_total, b_total) -> None:
    if b_total > 21:
        print('You Win!!! The bank went bust!')
    if b_total < 17:
        b_hand.append(DECK[random.randint(0, 13)])
        b_total = int(sum(b_hand))
        if b_total > 21:
            print('You Win!!! The bank went bust!')
    if b_total < p_total:
        print('You Win!!!')
    if b_total > p_total:
        print(f'You Lose the bank had {b_total}')
    if b_total == p_total:
        print('There is a DRAW!')


# TODO DEFINE ADDING UP THE SCORE

# TODO DEINE WIN OR LOSE CRITERIA

# Set up the required lists for the game.

# The Deck:


DECK: list = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

both_hands = deal_hand(DECK)
p_hand = both_hands[0]
b_hand = both_hands[1]

print(p_hand, b_hand)

fmt_hand = ''
for i in range(0, len(p_hand)):
    fmt_hand += str(p_hand[i]) + ', '
print(f'You have been dealt:\n\n*******\n{
      fmt_hand}\n*******\n\n and the dealer has been dealt:\n++++++\n+ {b_hand[1:len(b_hand)]} + \n++++++')
p_total = int(sum(p_hand))
b_total = int(sum(b_hand))
ht_stnd = input('Do you want to \'HIT\' or \'STAND\'').lower()
if ht_stnd == 'stand':
    stand(p_total, b_total)
    # if b_total > 21:
    #     print('You Win!!! The bank went bust!')
    # if b_total < 17:
    #     b_hand.append(DECK[random.randint(0, 13)])
    #     b_total = int(sum(b_hand))
    #     if b_total > 21:
    #         print('You Win!!! The bank went bust!')
    # if b_total < p_total:
    #     print('You Win!!!')
    # if b_total > p_total:
    #     print(f'You Lose the bank had {b_total}')
    # if b_total == p_total:
    #     print('There is a DRAW!')

while ht_stnd == 'hit':
    play_hit = in_play(p_hand, b_hand, DECK)
    p_hand = play_hit[0]
    b_hand = play_hit[1]
    p_total = int(sum(p_hand))
    b_total = int(sum(b_hand))
    fmt_phnd = ''
    fmt_bhnd = ''
    for i in range(0, len(p_hand)):
        fmt_phnd += str(p_hand[i]) + ', '
    for j in range(1, len(b_hand)):
        fmt_bhnd += str(b_hand[j]) + ', '
    print(f'Your hand is now:  {fmt_phnd}\n')
    ht_stnd = input('Hit or Stand? > ')

p_total = int(sum(p_hand))
b_total = int(sum(b_hand))
if b_total < 21:
    print(f'And the band has:  {b_hand}')
elif b_total > 21:
    print(f'The bank has {b_hand}')
elif b_total > 21 and p_total > 21:
    print('Yout both went BUST!!!')
    deal_hand(DECK)
elif p_total > 21:
    print('You Lose! You went BUST!!!')
    deal_hand(DECK)
elif b_total > 21 and p_total < 21:
    print('You Win! The bank went BUST!!!')
    deal_hand(DECK)
