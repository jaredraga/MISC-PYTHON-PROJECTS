#Guess The Number Game
#Flow Chart:

#        Produce answer
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


#This version doesn't ask the player's name if played again


#Note: code this game to 
#remember the player's name 
#after playing again

#also, just improve the rest 
#of the code in v5.0
#not in here so the documentation
#is legitimate

import random

def produceAnswer():
    number = random.randint(1, 20)
    
    return number    
    
def recordGuessesLeft(guessesTaken):
    guessesLeft = 6 - guessesTaken
    
    return guessesLeft

def getName():
    print()
    print('Hello, What\'s your name?')
    name = input()
    print()
    print('Well, ' + name + ', I\'m thinking of a number between 1 and 20.')
    
    return name
 
def makeGuess(guessesTaken):
    
    while guessesTaken < 6:
                       
        print('Take a guess')
    
        print('Guesses Left: ' + str(guessesLeft) + ' ')
    
        guess = input()
        guess = int(guess)        
        
        if guess < number:
            print('Your guess is too low')
            
        if guess > number:
            print('Your guess is too high')
            
        if guess == number:
            break
                
    return guess
def checkGuess(guess):    
    if guess == number:
        print('Good job, you guessed the number in ' + str(guessesTaken) + ' guesses.')
    if guess != number:
        print('Game Over')
        print('The number I was thinking of was ' + str(number))      

def playAgain():

    print()
    print('Play Again? (y/n)')
    
    return input().lower().startswith('y')

#Gets player name        
playerName = getName()
   
number = 0
playerName = ' '
guess = ' '
guessesTaken = 0
guessesLeft = 0
gameIsDone = False

while True:

    number = produceAnswer() 
    
    guess = makeGuess(guessesTaken)
    
    checkGuess(guess)
    
    playAgain()
    
    if gameIsDone:
        if playAgain():            
            guess = ' '
            guessesTaken = 0
            gameIsDone = False
            number = 0
    
        else:
            break
    
