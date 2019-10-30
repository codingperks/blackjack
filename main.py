# This is a blackjack simulator
# In this game, the player will draw a number of cards and attempt to beat the program, which also draws cards
# The player will have the option to hit or stick after being dealt two cards
# The player wins if they are closer to 21 than the computer, without going over 21


# random module used in order to draw cards from the deck
import random

# yes and no are defined for user input
yes = ["Yes", "yes", "Y", "y"]
no = ["No", "no", "N", "n"]

# hit and stick lists are also defined for user input
hit = ["Hit", "hit", "h", "H"]
stick = ["Stick", "stick", "S", "s"]


# Creating deck of cards
# this recreates the deck every repeat
def create_deck():
    global deck
    deck = []
    suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
    numbers = [i for i in range(2, 11)] + ['A', 'K', 'Q', 'J']
    for suit in suits:
        for number in numbers:
            deck += [str(number) + " of " + suit]


# This is the initial menu
def play_game():
    print("Would you like to play Blackjack?")
    while True:
        play_confirm = str(input("Yes or No?: "))
        if play_confirm in yes or play_confirm in no:
            if play_confirm in yes:
                return True
            else:
                return False
        else:
            print("Please type Yes or No" + "\n")
            continue


# this function draws the opening hand
def opening_hand(deck):
    random.shuffle(deck)
    for i in range(2):
        player_hand.append((deck.pop(0)))
        dealer_hand.append((deck.pop(0)))
    return


# this function allows a player to hit or stick
def draw_again():
    print("player hand:", player_hand)
    print("dealer hand: ['" + dealer_hand[0] + ", 'One face down']")
    while True:
        draw_confirm = str(input("Hit or stick?: "))
        if draw_confirm in stick or draw_confirm in hit:
            if draw_confirm in stick:
                return stick
            else:
                return hit
        else:
            print("Please type Hit or Stick" + "\n")
            continue


# this function returns the score for the player
def player_scoring():
    player_values = []
    score = []
    player_hand_names = player_hand[:]
    for i in player_hand_names:
        player_values.append(i.split(" ")[0])
    for i in player_values:
        if i == 'A':
            i = 11
        elif i == 'K' or i == 'Q' or i == 'J':
            i = 10
        else:
            i = int(i)
        score.append(i)
    player_score = sum(score)
    if player_score > 21 and 11 in score:
        ace = score.index(11)
        score[ace] = 1
    player_score = sum(score)
    return player_score


# this function returns the score for the dealer
def dealer_scoring():
    dealer_values = []
    score = []
    dealer_hand_names = dealer_hand[:]
    for i in dealer_hand_names:
        dealer_values.append(i.split(" ")[0])
    for i in dealer_values:
        if i == 'A':
            i = 11
        elif i == 'K' or i == 'Q' or i == 'J':
            i = 10
        else:
            i = int(i)
        score.append(i)
    dealer_score = sum(score)
    if dealer_score > 21 and 11 in score:
        ace = score.index(11)
        score[ace] = 1
    dealer_score = sum(score)
    return dealer_score


# this function compares both scores and prints a winner
def win(player_score, dealer_score):
    if player_score > 21:
        print("DEALER")
        return
    elif player_score < dealer_score <= 21:
        print("DEALER")
        return
    elif 21 > player_score > dealer_score:
        print("PLAYER")
        return
    elif dealer_score > player_score and dealer_score > 21 and player_score <= 21:
        print("PLAYER")
        return
    elif dealer_score == player_score and dealer_score <= 21 and player_score <= 21:
        print("TIE")
        return


# this function chooses dealer action based on simple dealer logic rules (<17 is a hit)
def dealer_game():
    while dealer_scoring() < 17:
        if dealer_scoring() < 17:
            print("Dealer hits")
            dealer_hand.append(deck.pop(0))
            input("Press enter to continue:")
            hands()
            continue
        else:
            break
    print("Dealer sticks")
    input("Press enter to continue:")
    hands()
    return


# this function prints player and dealer hands
def hands():
    print("Player hand:", player_hand)
    print("Dealer hand:", dealer_hand)


# this function runs the blackjack function and gives the option for player to restart
def main():
    while True:
        if blackjack() is False:
            break
        else:
            replay = input("Would you like restart? ")
            if replay in yes:
                print("\n")
                break
            elif replay in no:
                return None
            else:
                print("Please type yes or no")
                print("\n")
                continue
    main()


# this function controls blackjack sequencing and logic
def blackjack():
    create_deck()
    while True:
        global player_hand
        global dealer_hand
        player_hand = []
        dealer_hand = []
        opening_hand(deck)
        if play_game():
            while True:
                action = draw_again()
                if action == hit:
                    player_hand.append(deck.pop(0))
                    if player_scoring() > 21:
                        print("YOU LOSE: BUST")
                        hands()
                        return None
                    continue
                elif action == stick:
                    if player_scoring() > 21:
                        print("YOU LOSE: BUST")
                        hands()
                        return None
                    dealer_game()
                    break
            player_score = player_scoring()
            dealer_score = dealer_scoring()
            input("Press enter to reveal the winner:")
            win(player_score, dealer_score)
        break


if __name__ == "__main__":
    main()
