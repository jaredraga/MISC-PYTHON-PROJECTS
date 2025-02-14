#Guess the Number Game
#Doesn't bug out when player enters a letter

import random

guessesTaken = 0

number = random.randint(1, 20)

print('Hello! What is your name?')
myName = input()
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')

while guessesTaken < 6:
  
    print('Take a guess.') 
    guess = input()
    
    if guess not in '1234567890':
        print('Please enter a NUMBER')    
    
    elif int(guess) < number:
        print('Your guess is too low.')
        guessesTaken = guessesTaken + 1
        
    elif int(guess) > number:
        print('Your guess is too high')
        guessesTaken = guessesTaken + 1
        
    elif int(guess) == number:
        guessesTaken = guessesTaken + 1
        break
        
    guessesLeft = 6 - guessesTaken
    guessesLeft = str(guessesLeft)
  
    print('Guesses Left:' + guessesLeft + ' ')
 
 
if guess == number:
    guessesTaken = str(guessesTaken)
    
    print('Good Job, ' + myName + '.')
    
    if guessesTaken <= '1':
        print('You guessed the number in ' + guessesTaken + ' guess.') 
       
    if guessesTaken >  '1':
        print('You guessed the number in ' + guessesTaken + ' guesses.')


if guess != number:
    number = str(number)
    
    guessesTaken = str(guessesTaken)
    
    print('Guesses Taken:' + guessesTaken + ' ')
    print('Nope. The number I was thinking of was ' + number + '.')
