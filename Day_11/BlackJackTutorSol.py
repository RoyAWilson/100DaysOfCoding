'''
Tutor solution to Blackjack
'''

import random
import art


def deal_cards() -> list:
    '''
    Deal a hand of cards to a list
    '''
    cards: list = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card: int = random.choice(cards)
    return card


def calculate_score(cards: list) -> int:
    ''''
    Take a list of cards and return score
    0 for blackjack
    '''

    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(u_score, c_score) -> str:
    if c_score == u_score:
        return 'Draw'
    elif c_score == 0:
        return 'Lose! The opponent has Blackjack'
    elif u_score == 0:
        return 'Win! You have Blackjack'
    elif u_score > 21:
        return 'You lose! You went bust'
    elif c_score > 21:
        return 'Win! The opponent went Bust'
    elif c_score > 21 and u_score > 21:
        'No Score! You both went bust!'
    elif c_score < u_score:
        return 'Win!'
    else:
        return 'You lose!'


def play_game():

    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    gameover = False

    for i in range(2):
        user_cards.append(deal_cards())
        computer_cards.append(deal_cards())

    while not gameover:

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f'Your Cards:  {user_cards}, your score:  {user_score}')
        print(f'computer\'s first card: {computer_cards[0]}')
        if user_score == 0 or computer_score == 0 or user_score > 21:
            gameover = True
        else:
            user_should_deal = input(
                'type y to get another card or n to pass:  ').lower()
            if user_should_deal == 'y':
                user_cards.append(deal_cards())
                user_score = calculate_score(user_cards)
            else:
                gameover = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_cards())
        computer_score = calculate_score(computer_cards)

    print(f'\n\n\n\nYour final score is {
        user_score}\nand the computer\'s final score is {computer_score}\n')
    print(compare(user_score, computer_score))


while input('Do you want to play another game of Blackjack \'y\' or \'n\'').lower == 'y':
    print('\n'*20)
    play_game()
