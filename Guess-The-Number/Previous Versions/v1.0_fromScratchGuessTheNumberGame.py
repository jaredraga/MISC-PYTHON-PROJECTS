#Writing Guess The Number Game from scratch
#By -Me, The Duck

#imports the 'random' module
import random

#sets a variable named guessesTaken to 0. so you could count how many guesses were made by the player
guessesTaken = 0

#sets a variable that goes like this: guessesLeft(the turns you would like the player to have) minus guessesTaken. so that shows how make guesses left the player has.
guessesLeft = 3 - guessesTaken 

#sets variable named number that represents the answer. uses the random.randint module to make the computer think of a random number between 1 and 1 million
number = random.randint(1, 1000000)

#Asks the player to give their name and also declares the start of the guessing game
print()
print('Ey boi, Give ur name ples')
playerName = input()
print()
print('' + playerName + ', zat es very g0ad, let us start ze game.\nI\'m sinking of a number betweain 1 and 1 million.')

#creates a block that makes a loop with a condition that while the guessesTaken is less than the assigned number, proceed reading the code
while guessesTaken < 3:
   
    guessesLeft = str(guessesLeft) #turns the integer into a printable string
    
    #says how many guesses is left
    print('Guesses Left:' + guessesLeft + ' ')
    
    print()
    print('Guess ze number.')
    guess = input()
    guess = int(guess) #turns the guess into an integer, i dont know why
    
    #adds 1 everytime the player takes a guess
    guessesTaken = guessesTaken + 1
     
    #subtracts 1 everytime the player takes a fuxkin guess
    guessesLeft = 3 - guessesTaken
    
    #if the guess of the player is less than the answer, print this code
    if guess < number:
        print('m8 your guess is too low')
  
    #if the guess of the is greater tha. the answer, read this one
    if guess > number:
        print('your guess is too high m8')

    #if the guess of the PLAYER is EQUAL to the AnSWER BREAK off this LOOP
    #i dont know how the break fucking works but it works      
    if guess == number:
        break
    
if guess == number: #checks if the player guessed the answer
    guessesTaken = str(guessesTaken) #turns guessesTaken as an integer into a string. dunno why   
    number = str(number) #turns the answer as an integer into a string
    
    #congratulates the player and tells how many guesses he took
    print(' ey ' + playerName + ' u won m8 the right answer is indeed ' + number + ' m8 ')
    print('Guesses Taken:' +guessesTaken+ ' ')#

if guess != number: #checks if the player's guess is wrong
    number = str(number) #turns the answer as an integer into a string

    #says the right answer to the player
    print('nah m8 the number I was thinking of was ' + number + ' ')
    
    