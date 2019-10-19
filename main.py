# This is a blackjack simulator
# In this game, the player will draw a number of cards and attempt to beat the program, which also draws cards
# The player will have the option to hit or stick after being dealt two cards
# The player wins if they are closer to 21 than the computer, without going over 21

# random module used in order to draw cards from the deck
import random

# yes and no are defined for menu options
yes = ["Yes", "yes", "Y", "y"]
no = ["No", "no", "N", "n"]

hit = ["Hit", "hit", "h", "H"]
stick = ["Stick", "stick", "S", "s"]

# Creating deck of cards
suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
numbers = [i for i in range(2, 11)] + ['A', 'K', 'Q', 'J']
deck = []

for suit in suits:
    for number in numbers:
        deck += [str(number) + " of " + suit]

# Creating hands
playerhand = []
dealerhand = []

# This is the initial menu
def playgame():
    print("Would you like to play Blackjack?")
    while True:
        playconfirm = str(input("Yes or No?: "))
        if playconfirm in yes or playconfirm in no:
            if playconfirm in yes:
                return True
            else:
                return False
        else:
            print("Please type Yes or No" + "\n")
            continue


# this function draws the opening hand
def drawcards(deck, playerhand, dealerhand, turn):
    random.shuffle(deck)
    if turn == 1:
        for i in range(2):
            playerhand.append((deck.pop(0)))
            dealerhand.append((deck.pop(0)))
    else:
        playerhand.append(deck.pop(0))
        dealerhand.append(deck.pop(0))
    return


# this function allows a player to hit or stick
def drawagain(playerhand, dealerhand):
    print("player hand", playerhand)
    print("dealer hand", dealerhand)
    while True:
        drawconfirm = str(input("Hit or stick?: "))
        if drawconfirm in stick or drawconfirm in hit:
            if drawconfirm in stick:
                return stick
            else:
                return hit
        else:
            print("Please type Hit or Stick" + "\n")
            continue


# for card draws after hitting or sticking
def game(playerhand, dealerhand, action):
    if action == hit:
        playerhand.append(deck.pop(0))
        dealerhand.append(deck.pop(0))
        print("player hand", playerhand)
        print("dealer hand", dealerhand)
        return
    elif action == stick:
        dealerhand.append(deck.pop(0))
        print("player hand", playerhand)
        print("dealer hand", dealerhand)
        return


def main():
    while True:
        turn = 1
        if playgame():
            drawcards(deck, playerhand, dealerhand, turn)
            action = drawagain(playerhand, dealerhand)
            game(playerhand, dealerhand, action)
        else:
            return


if __name__ == "__main__":
    main()
