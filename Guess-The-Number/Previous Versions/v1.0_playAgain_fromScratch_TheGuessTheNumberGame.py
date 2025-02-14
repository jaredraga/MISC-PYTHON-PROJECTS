#Guess The Number Game
#Flow Chart:
            
#            Start

#        Introduce game        

#     Player guesses number
#  Player wins | Player loses
#                
#      Ask to play again
#repeat

import random #imports the module 'random'

def startGame(): #defines the start of the game block
    
    print('Please enter your name') #asks for the player's name
    playerName = input()
    
    print('Welcome, ' + playerName + '.') #greets player
    print('I\'m thinking of a number between 1 and 10')

#THIS is the bit where it asks the player to take a guess

    answer = random.randint(1, 10) #produces a random number between 1 and 10 for the answer

    guessesTaken = 0 #sets the guesses taken value to 0

    #makes an argument where if the guesses taken by the player is less than(<) 4, the code is read
    while guessesTaken < 4:
       
        guessesLeft = 3 - guessesTaken #subtracts the guesses left by the guesses taken
        
        guessesLeft = str(guessesLeft) #turns the interger of guesses left into a string
               
        print('Take a guess, ' + playerName + '') #prompts the player to take a guess
        guess = input()
        guess = int(guess) #turns the guess string into an integer
         #turns the integer input to a printable string

        print() #makes a blank line
        print('Guesses Left: ' + guessesLeft + '') #reads the guesses left to the player

        guessesTaken = guessesTaken + 1 #each time the player takes a guess this adds one to the guesses taken

        #if the guess of the player is too low, this code is read
        if guess < answer:
            print('Your guess is too low mate')
         
        #if the guess of the player is too high this one code is read   
        if guess > answer:
            print('Mate, your guess is too high')
         
                
           
#THIS is the bit where the game ends

    if guess == answer: #checks if the player guessed the correct answer
        answer = str(answer) #turns the number integer into a string
        guessesTaken = str(guessesTaken) #turns the guessesTaken integer to a string
        
            print('Nice Job mate, the correct answer is indeed ' + answer + ', you took ' + guessesTaken + ' guesses.')     
      
    if guess != answer: #checks if the player did not guess it correctly
        answer = str(answer) #turns the number integer into a string 
       
        print('Oi mate, what the fuck, you guessed wrongly')
        print('Mate, number I was thinking of was ' + answer + ' ')


playAgain = 'yes' #sets the value of playAgain to the string 'yes'
      
while playAgain == 'yes' or playAgain == 'y': #creates an argument where while the playAgain is equal to 'yes'/'y', the code is read      
    
    startGame()        
    
    print('Play Again? (y/n)') #asks if the player wants to play again
    playAgain = input()
        