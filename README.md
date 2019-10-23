# blackjack
23/10/2019

one player blackjack simulator, coded in python
  
What the program currently allows for:
    
    Opening menu to confirm that the user would like to use the program
    Opening hand is drawn (one card of dealer is hidden)
    Player can hit or stick
        Hit commands allow the player to hit or stick
        Stick commands score both hands and decides the winner
  
Functions:

     playgame(): Asks player if they want to play, N: exits the program
     drawcards(): draws opening hands
     drawagain(): hit or stick option
     playerscore(): returns the score for the player based on cards in hand
     dealerscore(): returns the score for the dealer based on cards in hand
     
 to make:
    
    dealeraction(): function to determine dealer logic depending on dealerscore()
    win(): function to determine winner (comparison of score)
    
    
long term to do:
    
    Clean up logic to improve efficiency
    Add betting functionality
    Clean code
    5 card rule?
    GUI / graphics ?