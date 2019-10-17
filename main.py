# This is a blackjack simulator
# In this game, the player will draw a number of cards and attempt to beat the program, which also draws cards
# The player will have the option to hit or stick after being dealt two cards
# The player wins if they are closer to 21 than the computer, without going over 21

# random module used in order to draw cards from the deck
import random

# yes and no are defined for menu options
yes = ["Yes", "yes", "Y", "y"]
no = ["No", "no", "N", "n"]

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
turn = 1

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
        i = 0
        for i in range(2):
            playerhand.append((deck.pop(0)))
            dealerhand.append((deck.pop(0)))
    else:
        playerhand.append(deck.pop(0))
        dealerhand.append(deck.pop(0))
    print("dealer hand ", dealerhand)
    print("player hand ", playerhand)
    return


# this function allows a player to hit or stick
def drawagain(playerhand, dealerhand):
    print("player hand", playerhand)
    print("dealer hand", dealerhand)
    hit = {"Hit", "hit", "h", "H"}
    stick = {"Stick", "stick", "S", "s"}
    drawconfirm = input("Hit or stick?: ")
    while True:
        if drawconfirm != stick or drawconfirm != hit:
            break
        else:
            return True
        return


'''def game(playerhand, dealerhand, hit, stick, turn, deck):
    if drawconfirm == hit:
        turn += 1
        drawcards()
    print("player hand", playerhand)
    print("dealer hand", dealerhand)
'''

def main():
    if playgame():
        drawcards(deck, playerhand, dealerhand, turn)
    else:
        return

if __name__ == "__main__":
    main()
