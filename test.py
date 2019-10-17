# file to test out code

import random

suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
numbers = [i for i in range(2, 11)] + ['A', 'K', 'Q', 'J']


deck = []

for suit in suits:
    for number in numbers:
        deck += [str(number) + " of " + suit]

playerhand = []
dealerhand = []
turn = 1

def drawcards(deck, playerhand, dealerhand, turn):
    random.shuffle(deck)
    if turn == 1:
        for i in range(2):
            playerhand.append((deck.pop(0)))
            dealerhand.append((deck.pop(0)))
    else:
        playerhand.append(deck.pop(0))
        dealerhand.append(deck.pop(0))
    print("dealer hand ", dealerhand)
    print("player hand ", playerhand)
    return

drawcards(deck, playerhand, dealerhand, turn)