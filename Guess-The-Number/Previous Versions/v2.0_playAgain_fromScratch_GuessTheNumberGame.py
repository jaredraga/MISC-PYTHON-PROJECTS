#Guess The Number Game
#Flow Chart:

#     Random number for answer
#      Record guesses taken          

#            Start

#        Introduce game        
#       Take player name

#   ↓ Player guesses number ↓
# Player wins  |  Player loses
#                
#      Ask to play again
#         

import random
import time

def gameAnswer():
    answer = random.randint(1, 20)

def guessesTaken():
    guessCount = 0
    
def gameIntro():
    name = ''    
    while name == '':
        print()
        print('Hello, What\'s your name?')
        name = input()
        time.sleep(0.4)
        print('Well, ' + name + ', I\'m thinking of a number between 1 and 20.')
        print()

def testName(theirName):
    theirName = str(theirName)

    blahblah = 0
    while blahblah == 0:
        
        print()
        print(''+theirName+'')
        print()
        
        blahblah = blahblah + 1
    
def takeGuess():
   
    while guessesTaken() < 6:
        
        print('Take a guess')
        guess = input()
        guess = int(guess)
        
        if guess < gameAnswer():
            print('Your guess is too low, mate.')
            
        if guess > gameAnswer():
            print('Your guess is too high,mate')
            
        if guess == gameAnswer():
            break
            
def checkGuess():
    guess = str(guess)
    #gameAnswer() = str(gameAnswer())
    #guessesTaken() = str(guessesTaken())
    
    if playerGuess() == gameAnswer():
        print('')
        
    if playerGuess() != gameAnswer:
        print('')    
         
    
playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':       
    
    playerName = gameIntro()
   
    testName(playerName)

    print('Play Again? (y/n)')
    playAgain = input()

