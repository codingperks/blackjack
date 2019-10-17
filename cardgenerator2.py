# This is an early script which lets the player draw as many cards as they choose from a deck

import random

yes = {"Yes", "yes", "Y", "y"}
no = {"No", "no", "N", "n"}

while True:
    _cards = input("Enter the number of cards you'd like to draw : ")
    print(_cards)
    try:
        _cards = int(_cards)
    except ValueError:
        print("Please enter an integer", "\n")
        continue

    if int(_cards) < 0 or int(_cards) > 52:
        print("Outside of range", "\n")
        continue
    else:
        suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
        numbers = [i for i in range(2, 11)] + ['A', 'K', 'Q', 'J']
        deck = []

        for suit in suits:
            for number in numbers:
                deck += [str(number) + " of " + suit]

        print(random.sample(deck, int(_cards)),"\n")

        while True:
            _continue = input("Would you like to draw another card? Please enter Yes or No: ")
            if _continue in yes or _continue in no:
                break
            elif _continue not in yes or _continue not in no:
                print("Please enter Yes or No" + "\n")
                continue
        if _continue in yes:
            continue
        else:
            break