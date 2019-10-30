# blackjack
30/10/2019
one player blackjack simulator, coded in python
  
What the program currently allows for:      

    Opening menu to confirm that the user would like to use the program    
    Opening hand is drawn (one card of dealer is hidden)
    Player can hit or stick
        Hit commands draw a card for the player and then asks the player if they'd like to hit or stick
			Iff the player's score goes over 21, they bust and a loss screen is shown, they are given the option to play again
		Stick commands start the dealer logic
			If the dealer's score is below 17, they hit
			If the dealer's score is above 17, they stick
	Once both the dealer and player have stuck, their scores are compared using blackjack scoring to reveal the winner
	
The scoring follows blackjack rules:

	Dealer wins if any of the following occurs:
		playerscore > 21
		21 => dealerscore & dealerscore > playerscore
	Player wins if:
		21 => playerscore > dealerscore
		21 => playerscore & dealerscore > 21
	There is a tie if:
		playerscore == dealerscore and dealerscore <=21 and playerscore <=21
  
Functions:

	 main(): contains blackjack game and option for player to repeat
		 blackjack(): Runs blackjack sequence and logic
		     create_deck(): creates and shuffles deck
			 play_game(): Asks player if they want to play, N: exits the program
			 opening_hand(): draws opening hands
			 draw_again(): hit or stick option
			 player_scoring(): returns the score for the player based on cards in hand
			 dealer_scoring(): returns the score for the dealer based on cards in hand
			 dealer_game(): this chooses dealer action based on simple dealer logic rules (<17 is a hit)
			 hands(): this prints dealer's hand and player's hand    
			 win(): compares player and dealers core and prints winner

    
long term to do:    

    Add betting functionality
    Clean up logic to improve efficiency
        Remove any duplicates
        Make namespace efficient
    General cleaning and documentation
    5 card rule?
    Multiplayer?
    GUI / graphics (?)







ARCHIVE
23/10/2019

one player blackjack simulator, coded in python
  
What the program currently allows for: 

    Opening menu to confirm that the user would like to use the program
    Opening hand is drawn (one card of dealer is hidden)
    Player can hit or stick
        Hit commands draw card and then asks the player if they'd like to hit or stick
        Stick commands score both hands and decides the winner
  
Functions:

     playgame(): Asks player if they want to play, N: exits the program
     openinghand(): draws opening hands
     drawagain(): hit or stick option
     playerscore(): returns the score for the player based on cards in hand
     dealerscore(): returns the score for the dealer based on cards in hand
         
    
long term to do:    

    Clean up logic to improve efficiency
    Add betting functionality
    Clean code
    5 card rule?
    GUI / graphics ?
