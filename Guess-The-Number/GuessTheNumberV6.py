#Guess The Number Game V5

#!duck

#Flow Chart

#!!!!!!!
# Start
# Think of an Answer
# Get Player Name
# Player Guesses The Answer
# Remember Guesses Taken
# Player Wins/Player Loses
# End/Play Again
#!!!!!!!
# Flow Chart V2:
#Start
#Player chooses difficulty
#Think of an answer
#Greet player
#Player takes a guess
#Player Wins/Loses
#Game Ends/Player plays again
#!!!!!!! 


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

#4/30/18 ! Alright I'm satisfied with this code
#5/4/18 ! Holy fuck this code looks ugly. So much fucking redundancy!


#Statistics
#Average Tries Before Correct Answer
#on Easy Mode: 3!4 guesses (4)
#on Medium: 5!6 (5)
#on Hard Mode: 5!6 (4)
import random

print('''
=== === === ===== === === ===
    Game: Guess The Number
==== ==== ==== ==== ==== ====
           Welcome
=== === === ===== === === ===
''')


 

#FIX the ARRANGEMENT of the goddamned functions
#//Fixed 

#Make a code that changes the amount of available guesses depending on the difficulty(done√)
#also display the guesses left of that
#//Done

#Fuck this function is not working it loops forever even if I give a proper answer
#//Holy shit I fixed it.
#Lets player choose difficulty    

#//v6.0 5/14/18
#//Holy fuck this code is so inefficient and garbage!looking.
#//I'm gonna replace those nasty repeating if statements with a single for loop.

def chooseDifficulty():
    while True:
        print('''
==== ==== ==== ==== ==== ====
    Choose the difficulty:
==== ==== ==== ==== ==== ====
    Easy | Medium | Hard
==== ==== ==== ==== ==== ====
''')
        print('           ',end = '')
        difficulty = input()
     
        if difficulty.lower().startswith('e'):
            difficulty = 'Easy'
            secretAnswer = random.randint(1, 10)
            maximumAnswer = 10
            maxGuessesAvailable = 4
            answerRange = '1 and 10'
            scoreToAdd = 5
            scoreToSubtract = 1
            #return difficulty
            break
        elif difficulty.lower().startswith('m'):
            difficulty = 'Medium'
            secretAnswer = random.randint(1, 30)
            maximumAnswer = 30
            maxGuessesAvailable = 5
            answerRange = '1 and 30'
            scoreToAdd = 10
            scoreToSubtract = 2
            #return difficulty
            break          
        elif difficulty.lower().startswith('h'):
            difficulty = 'Hard'
            secretAnswer = random.randint(1, 50)
            maximumAnswer = 50
            maxGuessesAvailable = 4
            answerRange = '1 and 50'
            scoreToAdd = 15
            scoreToSubtract = 3
            #return difficulty
            break
        #if the player didn't type a difficulty mode i.e. '123$%' or 'George W. Bush'    
        #it makes the player enter type again until they enter a proper answer        
        else:
            print()
            print('''
===== ===== ===== ==== ===!!!
 Please Enter proper answer:
 e for 'Easy' 
 m for 'Medium' 
 h for 'Hard'
===== ===== ===== ==== ===!!!''')     
    
    minimumAnswer = 1
    return difficulty, secretAnswer, minimumAnswer, maximumAnswer, maxGuessesAvailable, answerRange, scoreToAdd, scoreToSubtract


def getScore(score ,scoreToAdd, guess, secretAnswer):
    
    scoreToAddDependingOnGuessesTaken = (maxGuessesAvailable - guessesTaken * scoreToAdd)

    if guess != secretAnswer:
        score = score - scoreToSubtract - scoreToAddDependingOnGuessesTaken

    elif guess == secretAnswer:
        score = score + scoreToAdd + scoreToAddDependingOnGuessesTaken

    return score


#displays chosen difficulty
#I'm using the format() function to display the variables in a multi line
def displayAllStats(difficulty, maximumAnswer, maxGuessesAvailable):
    print('''
===========================!!
 Difficulty      = {diffHere}
===========================!!
 Minimum Answer  = 1
===========================!!
 Maximum Answer  = {maxAnswerHere}
===========================!!
 Maximum Guesses = {maxGuessesAvailableHere}
===========================!!'''.format(diffHere = difficulty, maxAnswerHere = maximumAnswer, maxGuessesAvailableHere = maxGuessesAvailable))

           
def gameIntro(answerRange):
    
    print('''
---- ---- ---- ---- ---- ----
   I'm thinking of a number 
    between {answerRangeHere} 
---- ---- ---- ---- ---- ----
    '''.format(answerRangeHere = answerRange))

def getGuess(minimumAnswer, maximumAnswer):
    # This function returns the number the player entered 
    # Note: Function requires input validation for non-numeric characters
    # i.e. special characters or text input
    #
    # Known issues: Game breaks if input contains:
    # - numbers with operators (like 1 + 1)
    # - numbers followed by symbols (like '1 P' or '1@' or '1 $')
    
    while True:                                              
        print('''
     ====== ====== ======
         Take a guess:   
     ====== ====== ======''')
        print('        ',end = '')
        guess = input()
        #makes sure player entered a number
        guessIsAllNumber = False
        for i in range(len(guess)): #checks if guess is all numbers

            if guess[i] in '0123456789': #if every character in guess is a number != guessIsAllNumber is True
                guessIsAllNumber = True

            else:
                guessIsAllNumber = False #if not... the player is prompted to make a correct answer!!one with just numbers in it

        if guessIsAllNumber: #if guessIsAllNumber is True != it checks if player entered a number too low/too high(like !24 or 1000)
            guess = int(guess)

            if guess < minimumAnswer:
                print('''

----  ----  ----  ----  ----  ----  ----  ----
    The minimum number you can answer is {minimumAnswerHere}
----  ----  ----  ----  ----  ----  ----  ----'''.format(minimumAnswerHere = minimumAnswer))

            elif guess > maximumAnswer:
                print('''
                    
----  ----  ----  ----  ----  ----  ----  ----
    The maximum number you can answer is {maximumAnswerHere}
----  ----  ----  ----  ----  ----  ----  ----'''.format(maximumAnswerHere = maximumAnswer))
            else:
                return guess #returns if there's nothing wrong with the guess

        else:
            print('''
----- ----- ----- ----- -----
  Please only enter NUMBERS
 No special characters i.e
 ($ / % / * / A / @ / + / &)
----- ----- ----- ----- -----
                ''')
   
def checkGuess(guess, secretAnswer, guessesTaken, score, maxGuessesAvailable, gameIsDone):
    
    if guess < secretAnswer:
        print('''
----- ----- ----- ----- -----
    Your guess is too LOW
----- ----- ----- ----- -----''')
        
    elif guess > secretAnswer:
        print('''
----- ----- ----- ----- -----
   Your guess is too HIGH
----- ----- ----- ----- -----''')

    elif guess == secretAnswer:        
        print('''
===== ===== ===== ===== =====
       $$$ You WON $$$
    You guessed the number
        in {guessesTakenHere} guess(es)
===== ===== ===== ===== =====
         Score:{scoreHere}
===== ===== ===== ===== ====='''.format(guessesTakenHere = guessesTaken, scoreHere = score))
        gameIsDone = True
        return gameIsDone

    elif guessesTaken >= maxGuessesAvailable and guess != secretAnswer:
        print(''' 
===== ===== ===== ===== =====
           You LOST
    The number that I was 
      thinking of was 50{secretAnswerHere}
===== ===== ===== ===== =====
         Score:{scoreHere}
===== ===== ===== ===== ====='''.format(secretAnswerHere = secretAnswer, scoreHere = score))
        gameIsDone = True
        return gameIsDone

def playAgain():
    # Asks if player wants to play again
    print(''' 
======= ====== ====== =======
  Do you want to Play Again?
          Yes | No
======= ====== ====== =======''')
    print('            ', end = '')
    return input().lower().startswith('y')
    
playerName = 'Unknown'
guessesTaken = 0
difficulty, secretAnswer, minimumAnswer, maximumAnswer, maxGuessesAvailable, answerRange, scoreToAdd, scoreToSubtract = chooseDifficulty()
score = 0
displayAllStats(difficulty, maximumAnswer, maxGuessesAvailable)
gameIntro(answerRange)
gameIsDone = False #set gameIsDone to False so it loops until player wins/loses
gamesPlayed = 0
while True:


    #fuck it's bugging out. it's not exiting when game is already done and the score also doesn't increase again for some reason
    
    while guessesTaken <= maxGuessesAvailable:
        
        guess = getGuess(minimumAnswer, maximumAnswer)
        
        #adds 1 everytime player takes a valid guess        
        guessesTaken = guessesTaken + 1     

        gameIsDone = checkGuess(guess, secretAnswer, guessesTaken, score, maxGuessesAvailable, gameIsDone)

        score = getScore(score, scoreToAdd, guess, secretAnswer) #it's not working for some reason... //update 5/17/18 it's working now just had to put 'score =' at the front of it        
        
        if guessesTaken >= maxGuessesAvailable:
            gameIsDone = True
            break
        # Ask the player if they want to play again (but only if the game is done
    if gameIsDone:
        gamesPlayed = gamesPlayed + 1
        if playAgain(): 
            guessesTaken = 0 
            difficulty, secretAnswer, minimumAnswer, maximumAnswer, maxGuessesAvailable, answerRange, scoreToAdd, scoreToSubtract = chooseDifficulty()
            displayAllStats(difficulty, maximumAnswer, maxGuessesAvailable)     
            gameIntro(answerRange)  
            gameIsDone = False 
        else: 
            break

print('''
====== ===== ======
     Game Over
====== ===== ======
 Player:{playerNameHere}
====== ===== ======
 Score:{scoreHere}
====== ===== ======'''.format(scoreHere = score, playerNameHere = playerName))