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


# def in_play(plyr_hand, bnk_hnd, dck) -> tuple:
#     '''
#     To deal further cards if necessary
#     arguments: plyr_hand LIST hand, bnk_stnd LIST, dck LIST

#     '''
#     plyr_hand.append(dck[random.randint(0, 12)])
#     bnk_hnd.append(dck[random.randint(0, 12)])
#     return plyr_hand, bnk_hnd


def form_hands(player_hand, bank_hand) -> tuple:
    plyr_hand = ''
    bnk_hnd = ''
    for i in range(0, len(player_hand)):
        plyr_hand += str(player_hand[i]) + ', '
    for j in range(1, len(bank_hand)):
        bnk_hand = str(bank_hand[j]) + ', '
    print(plyr_hand)
    return plyr_hand, bnk_hand


def win_lose(pscore: int, bscore: int) -> str:
    mess = ''
    if pscore > 21:
        mess = 'You lose! You have gone bust!'
    elif bscore > 21:
        mess = 'You win! Bank has gone bust'
    elif bscore > 21 and pscore > 21:
        mess = 'You have both gone bust!'
    elif pscore == bscore:
        mess = 'There is a draw!'
    elif bscore > 21 and pscore <= 21:
        mess = 'You win.  The bank has gone bust!'
    elif bscore > pscore:
        mess = 'Bank wins!'
    elif pscore > bscore:
        mess = 'You win!'
    return mess


def hit(plyr_hnd, bnk_hnd):
    if sum(dealt[1]) < 17:
        dealt[1].append(DECK[random.randint(0, 12)])
    dealt[0].append(DECK[random.randint(0, 12)])
    return plyr_hnd, bnk_hnd


DECK = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def start_game():
    dealt: list = deal_hand(DECK)
    player_hand: str = str(dealt[0])
    bank_hand: str = str(dealt[1][1:])
    out = [dealt, player_hand, bank_hand]
    print(f'************************************\nYou have been dealt: {
        player_hand}\n************************************\n\n')
    print(f'_______________________\nBank hand  {
        bank_hand}\n_______________________\n')
    return out


play = True
while play is True:
    game = start_game()
    dealt = game[0]
    player_hand = game[1]
    bank_hand = game[2]

    player_score: int = int(sum(dealt[0]))
    bank_score: int = int(sum(dealt[1]))
    stnd_hit = input('Do you want to \'stand\' or \'hit\'? > ')

    while stnd_hit == 'hit':
        while bank_score <= 13:
            dealt[1].append(DECK[random.randint(1, 11)])
            bank_score = int(sum(dealt[1]))
        updated_hands = hit(dealt[0], dealt[1])
        player_score = int(sum(dealt[0]))
        bank_score = int(sum(dealt[1]))
        print(updated_hands[0], updated_hands[1])
        stnd_hit = input('Do you want to \'stand\' or \'hit\'? > ')
    player_score = int(sum(dealt[0]))
    bank_score = int(sum(dealt[1]))
    message = win_lose(player_score, bank_score)
    print(f'\n\n*******************************************************\nYour final hand:  {dealt[0]}, scoring {
        player_score}\n\nbank final hand: {dealt[1]}  giving a final score of {bank_score}\n\n{message}\n*******************************************************\n\n')

    print(message)
    play = input('Play again? y/n? > ').lower()
    if play == 'n':
        play = False
    else:
        play = True
