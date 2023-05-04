from auction_art import logo


def clear():
    print(chr(27) + "[2J")


print(logo)
print('Welcome to the silent auction.')

bidders = True
bids = {}


def find_winner():
    max = 0
    winner = ''
    for name in bids:
        if bids[name] > max:
            max = bids[name]
            winner = name
    print(
        f"The winner of the auction is {winner} and the bid was {bids[winner]}.\n")


while bidders:
    name = input('Please enter your name:  ')
    bid = int(input('Please enter your bid amount:  $'))
    bids[name] = bid
    new_bidder = input('Is there another bidder? "yes" or "no".  ')
    if new_bidder == 'no':
        bidders = False
        find_winner()
    else:
        clear()
