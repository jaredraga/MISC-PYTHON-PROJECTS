#Guess The Number Game V5

#-duck

#Flow Chart

#-------
# Start
# Think of an Answer
# Get Player Name
# Player Guesses The Answer
# Remember Guesses Taken
# Player Wins/Player Loses
# End/Play Again
#-------
# Flow Chart V2:
#Start
#Player chooses difficulty
#Think of an answer
#Greet player
#Player takes a guess
#Player Wins/Loses
#Game Ends/Player plays again
#------- 


#Problems: 
#Can't produce answer
#Faulty guess checking
#Not counting guesses taken
#Not congratulating player
#//These problems are fixed

#Code This:
#Ask what difficulty they want
#Easy | Medium | Hard
#//Done. This feature is implemented

#Add a little bit of ASCII art in the game.

#add god mode easter egg when player enters name 'god/godmode',just because I want to
#//Done, and that fuckin' shite was fun

#MAKE function that combines all stats together into one block
#Difficulty:
#Guesses Available:
#Answer Range:
#Previous Answer:
#Guesses Left:
#Minimum Answer:
#Maximum Answer:
#//DONE√

#4/30/18 - Alright I'm satisfied with this code
#5/4/18 - Holy fuck this code looks ugly. So much fucking redundancy!


#Statistics
#Average Tries Before Correct Answer
#on Easy Mode: 3-4 guesses (4)
#on Medium: 5-6 (5)
#on Hard Mode: 5-6 (4)
import random

print('Game: Guess The Number')
print()

 
        
#FIX the ARRANGEMENT of the goddamned functions
#//Fixed 

#Make a code that changes the amount of available guesses depending on the difficulty(done√)
#also display the guesses left of that
#//Done

#Fuck this function is not working it loops forever even if I give a proper answer
#//Holy shit I fixed it.
#Lets player choose difficulty

#//v6.0 5/14/18 
#//Holy fuck this code is so inefficient and garbage-looking. I'm gonna replace those nasty repeating if statements with a single for loop    
def chooseDifficulty():
    while True:
        print('Choose the difficulty:')
        print('(E)asy | (M)edium | (H)ard')
        difficulty = input()
        
        if difficulty.lower().startswith('e'):
            difficulty = 'easy'
            #return difficulty
            break
        elif difficulty.lower().startswith('m'):
            difficulty = 'medium'
            #return difficulty
            break          
        elif difficulty.lower().startswith('h'):
            difficulty = 'hard'
            #return difficulty
            break
        #if the player didn't type a difficulty mode i.e. '123$%' or 'George W. Bush'    
        #it makes the player enter type again until they enter a proper answer        
        else:
            print()
            print('Please enter PROPER answer.')     
    return difficulty

# Chooses Secret Answer depending on the chosen difficulty
def getSecretAnswer(difficulty):
    if difficulty == 'easy':
        number = random.randint(1, 10)
    if difficulty == 'medium':
        number = random.randint(1, 30)
    if difficulty == 'hard':
        number = random.randint(1, 50)  
        
    return number

def getMaximumAnswers():
    if difficulty == 'easy':
        maximumAnswer = 10
    if difficulty == 'medium':
        maximumAnswer = 30
    if difficulty == 'hard':
        maximumAnswer = 50
        
    return maximumAnswer


def getMaximumGuessesPlayerCanTake():
    if difficulty == 'easy':
        maxGuesses = 4
    if difficulty == 'medium':
        maxGuesses = 5
    if difficulty == 'hard':
        maxGuesses = 4
        
    return maxGuesses

#displays chosen difficulty
def displayDifficulty():
    print()
    print('Difficulty:', end= ' ')
    if difficulty == 'easy':
        print('Easy')
    if difficulty == 'medium':
        print('Medium')
    if difficulty == 'hard':
        print('Hard')

def displayGuessesAvailable():
    print('Guesses Available:' +str(maximumGuessesPlayerCanTake))
    
#greets player with greetings the computer chooses
def greetingPlayer():
        
    #GREETINGS = ['Hello!', 'Hi', 'Hey!', 'Heyoo', 'Yo!']
    #choosesRandomGreetings = random.randint(0, 4)
    #chosenGreetings = GREETINGS[choosesRandomGreetings]
    #//Deleted this shite. This function fuckin' looks ugly m
    #//Replaced with 'Type your name.' prompt instead
    
    print('-')
    print('Type your name:')
    #playerName = input()#disabling this input while testing
    playerName = 'Jesus'
    
    if playerName.lower() == 'god':
        return playerName.lower()
    elif playerName.lower() == 'admin': 
        return playerName.lower()      
    else:
        return playerName

                
def gameIntro():
    
    print(' ' * 1000)
    print('Hello,' + playerName)    
    print('I\'m thinking of a number between ', end= ' ')
    
    if difficulty == 'easy':
        print('1 and 10')
    if difficulty == 'medium':
        print('1 and 30')
    if difficulty == 'hard':
        print('1 and 50')


def displayAllStats():
    if guessesTaken >= 1:
        print('Previous Answer:\'' + str(guess) + '\' ')
    print('Guesses Available:' +str(maximumGuessesPlayerCanTake))
    
    print('Max Answer:' + str(maximumAnswer) )
    print('Min Answer:' + str(minimumAnswer) )
           
    print('Guesses Taken:' + str(guessesTaken) )


def getGuess():
    # This function returns the number the player entered 
    # P.S this function bugs out if the player entered a letter or a symbol i.e. 'Leet 'Lil Bitch' or '$$$'
    #//Holy fuck I fixed it
    
    # Holy fuck the game breaks 
    # if I answer
    # any and all numbers with operators like 1 + 1
    # fuck, and also any and all answers beginning with numbers and then symbols like '1 P' or '1@' or '1 $'
   
    while True:        
        print('Guesses Left:' + str(maximumGuessesPlayerCanTake - guessesTaken))
        if guessesTaken == 0:
            print('Take a guess')
        else:
            print('Guess again')        
        print()        
        guess = input()                                        
        
        #makes sure player entered a number
        guessIsValid = False
        for i in range(len(guess)):
            if guess[i] in '0123456789':
                guessIsValid = True                   
        
        else:
            guessIsValid = False
            print('Please only enter NUMBERS!')
    
        if guessIsValid:
            guess = int(guess)
        
            if guess < 5:
                print('No guess less than 5!')
            
        elif guess > 50:
            print('No guess more than 50!')
                 
        else:
            break
   
        if guessesTaken == 0:
            print('Previous Answer:\'' + str(guess) + '\' ')
      
def checkGuess():
    while True:
        print(' ' * 3000)
        if guess < secretAnswer:
            print('Your guess is too low')
        
        elif guess > secretAnswer:
            print('Your guess is too high')
               
        return
        
    
def confirmAnswer():
    dash = '-' * len(playerName)
    if guess == secretAnswer:        
        print('-------------' + dash)
        print('-YOU WON!, ' + playerName + ' -')
        print('-------------' + dash)	     
        
        if guessesTaken == 1:
            print('You guessed the number in ' + str(guessesTaken) + ' guess')        
        else:
            print('You guessed the number in ' + str(guessesTaken) + ' guesses')
            
        print('Guesses Left:' + str(maximumGuessesPlayerCanTake - guessesTaken))   
            
  
    elif guess != secretAnswer:
        print()
        print('-------------' + dash)
        print('-YOU LOST!, ' + playerName + ' -')
        print('-------------' + dash)	     
        print('the number I was thinking of was ' + str(secretAnswer) + ' ')
    
    return
  
           
def playAgain():
    # Asks if player wants to play again
    print()
    print('Do you want to play again?')
    print()
    #print('Player Name: ' + playerName + ' ')#Removed this code because it looks awkward
    return input().lower().startswith('y')

def welcomeBackPlayer():
    dash = '-' 
    print(' ' * 2500)#just prints many spaces
    #Adds dash to the ASCII art depending on the length of the player name
    print('-----------------' + dash * len(playerName))
    print('-Welcome Back, ' + playerName + ' -')
    print('-----------------' + dash * len(playerName))	     
    print()
    print('Again, I am thinking of a number between', end = ' ')
    if difficulty == 'easy':
        print('1 and 10')
    if difficulty == 'medium':
        print('1 and 30')
    if difficulty == 'hard':
        print('1 and 50')

import time
#easter egg
def godModeDisplay():

    text = 'Loading...'
    dot = '•' * len(text)
    cycle = 0
    while True:       
        for i in range(len(text)):
            cycle = cycle + 1
            print(' ' * 3000)
            print(text[:i] + dot[i] + text[i+1:])    
            time.sleep(0.1)                          
            
            if cycle >= 12 * 3:
                return

            #well what the fuck that was weird
            #it doesn't fucking stop            
            #//Fixed it, just made a new function
                     
def greetGM():
    print(' ' * 10000)
    print('''Warning:Game Masters only
    	
Warning:Administrators only
    	
Welcome,
    
Please authenticate:

User:Admin
Input your password:''')
    while True:
        print(':', end = '')
        pWord = input()
        if pWord == 'admin':
            time.sleep(1)
            break
        else:
            time.sleep(0.6)
            print('Password Incorrect')
    print('''
Authentication Successful...''')
    time.sleep(3)
    print(' ' * 3000)
    print('''
Source Code Editing Shell

Warning: Back-up entire code before editing Source Code

Warning: Authorized Administrator Only
     	    	
Enter your command:''') 
    	
    while True:
        print('$root@localhost/dir:', end = '')
        command = input()
        time.sleep(0.8)
        if command == '--exit':
            print()
            print('Terminating session...')
            time.sleep(3)
            print(' ' * 3000)
            print('SESSION TERMINATED')
            print('Press \'enter\' to continue')
            input()
            return 
        else:
            print('Error:\'' + command + '\' is not a command. \nSee \'$2FA Password$ --help or --exit to exit\' ')


               
guessesTaken = 0
difficulty = chooseDifficulty()
maximumGuessesPlayerCanTake = getMaximumGuessesPlayerCanTake()
minimumAnswer = 1
maximumAnswer = getMaximumAnswers()
secretAnswer = getSecretAnswer(difficulty)
displayDifficulty()
displayGuessesAvailable()
playerName = greetingPlayer()
if playerName == 'god' or playerName == 'admin':
    cycle = 0
    godModeDisplay()
    greetGM()
gameIntro()
gameIsDone = False

#loops until game is done
#
while True:

    while guessesTaken < maximumGuessesPlayerCanTake:
        displayAllStats()
        
        guess = getGuess()
        
        #adds 1 everytime player takes a guess              
        guessesTaken = guessesTaken + 1

        checkGuess()
        
        if guess == secretAnswer:
            break            

    while True:
        confirmAnswer()
    
        gameIsDone = True
        
        break
        
    # Ask the player if they want to play again (but only if the game is done
    if gameIsDone: 
        if playAgain(): 
            guessesTaken = 0
            
            gameIsDone = False 
            secretAnswer = getSecretAnswer(difficulty)
            welcomeBackPlayer()
        else: 
            break