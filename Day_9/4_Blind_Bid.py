'''
produce a dictionary to hold closed bids
program should ask if any more bidders
clear screen - by scrolling 100 times
return highest bid when no more bidders.

Probably quicker and easier to use max(dictionary)
'''


def get_bid() -> tuple:
    '''
    Get the name and the amount to bid.
    '''

    name = input('Please enter your name:  > ')
    bid = float(input('How much do you bid? > £'))
    return name, bid


def winning_bid(bid_dict) -> str:
    val: float = 0.0
    winning_bid: str = ''

    for key in bid_dict:
        amt = bid_dict[key]
        if amt > val:
            val = amt
            winning_bid = key
    return f'The winning bid of £{val} was made by {winning_bid}'


bid_dict: dict = {}
gavel = '''                         ___________              
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                         `'-------'`
                       .-------------.
                   jgs/_______________\\'''

enter_bidder: str = 'yes'
print(gavel)
while enter_bidder == 'yes':
    print('\n' * 50)
    print(gavel)
    details = get_bid()
    bid_name = details[0]
    bid_amount = details[1]
    bid_dict[bid_name] = bid_amount
    d = input('does anyone else want to bid (yes/no)? > ').lower()
    enter_bidder = d
    print('\n' * 50)

print(gavel)

winner = winning_bid(bid_dict)
print(winner)
