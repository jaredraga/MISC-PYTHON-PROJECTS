#This is the first game I created in Python!
#Guess the Number Game
import random

guessesTaken = 0

number = random.randint(1, 20)

print('Hello! What is your name?')
myName = input()
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')

while guessesTaken < 6:
  
    print('Take a guess.') 
    guess = input()
    guess = int(guess)
          
        
    guessesTaken = guessesTaken + 1

    if guess < number:
        print('Your guess is too low.')

    if guess > number:
        print('Your guess is too high')

    if guess == number:
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
    