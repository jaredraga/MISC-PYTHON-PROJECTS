#Typing from memory
#No search

import random

guessesTaken = 0

number = random.randint(1, 30)

print()
print('Hello, What\'s your name?')
print()
myName = input ()
print()
print('Oh, ' + myName + '?, \nI\'m thinking about a number between 1 and 30')

while guessesTaken < 10:
    
    if guessesTaken == 0:
        
        print('Give it a guess')
        print()
        guess = input()
        guess = int(guess)

    else:
        print()
        print('Guess:', end=' ')
        guess = input()
        guess = int(guess)
        
    guessesTaken = guessesTaken +1

    if guess < number:
        print()
        print('Your guess is too low')
        
    if guess > number:
        print()
        print('Your guess is too high')
        
    if guess == number:
        break
        
    guessesLeft = 10 - guessesTaken
    guessesLeft = str(guessesLeft)
    print('Guesses Left: ' + guessesLeft + ' ')       

if guess == number:
    print()
    print('grats mate')
    
if guess != number:
    print()
    print('nah mate')
print()   
guessesTaken = str(guessesTaken) 
print('Guesses Taken:' + guessesTaken + ' ')      