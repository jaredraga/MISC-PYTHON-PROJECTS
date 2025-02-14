#Guess The Number Game
#Flow Chart:

#     Random number for answer
#      Record guesses taken          
#      Record guesses left

#            Start

#        Introduce game        
#       Take player name

#   ↓ Player guesses number ↓
# Player wins  |  Player loses
#                
#      Ask to play again
#         

#imports the random module
import random

#creates a random number between 1 and 20 for an answer
numberAnswer = random.randint(1, 20)

#creates variable 'guessesTaken' and set value to 0
guessesTaken = 0

#creates variable 'guessesLeft'
guessesLeft = 6 - guessesTaken

  
#makes a function 'checkAnswer()'     
def checkAnswer():
    #checks if guess is equal to the answer
    if guess == numberAnswer:        
        print('Good job, you guessed the right answer in ' + str(guessesTaken) + ' guesses!') 
    
    #checks if guess is not equal to the answer
    if guess != numberAnswer:
        print('Game over, the right answer is ' + str(numberAnswer) + '.')
     
    #'return' keyword makes the computer exit from the function
    return   

#creates variable 'playAgain' and sets its value to 'yes' (string value of yes)  
playAgain = 'yes'

#makes a loop with while condition that; while playAgain is equal to 'yes' or 'y'; the loop is played until condition is false
while playAgain == 'yes' or playAgain == 'y':

    #asks for player's name and records player input to variable 'playerName'
    print('Hello, What\'s your name?')
    playerName = input()
    print('Well, ' + playerName + ', I\'m thinking of a number between 1 and 20.')
    
    #makes a loop with while condition that; while guessesTaken is greater than six; the loop is played until condition is false    
    while guessesTaken < 6:
    
        #tells player to "Take a guess"
        print('Take a guess')
        #says the number of guesses left in string value
        print('Guesses Left: ' + str(guessesLeft) + ' ')
        #the guess of the player is recorded in variable 'guess'
        guess = input()
        #the variable 'guess' is turned into an integer
        guess = int(guess)
    
        #everytime player takes a guess; guessesTaken count is added by 1
        guessesTaken = guessesTaken + 1
    
        #the 'if' conditions checks the player's guess
        if guess < numberAnswer:
            print('Your guess is too low, mate.')
        
        if guess > numberAnswer:
            print('Your guess is too high, mate.')
        
        if guess == numberAnswer:
            #'break' keyword makes the computer exit from the loop
            break    
        
    #calls the 'checkAnswer()' function   
    checkAnswer()
    
    #asks if player wants to play again
    print('Play Again? (yes/no)')
    playAgain = input()
