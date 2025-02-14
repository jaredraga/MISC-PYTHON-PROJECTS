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

print('''
====== ====== ====== ====== ======
      Game: Guess The Number
====== ====== ====== ====== ======
            Welcome
====== ====== ====== ====== ======

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
#//Holy fuck this code is so inefficient and garbage-looking.
#//I'm gonna replace those nasty repeating if statements with a single for loop.

def chooseDifficulty():
    while True:
        print('''
                #### #### #### #### #### ####
                   Choose the difficulty:
                #### #### #### #### #### ####
                    Easy | Medium | Hard
                #### #### #### #### #### ####

                Default Difficulty: 'Easy'
               ''')
        print('           ',end = '')
        difficulty = input()
        
        if difficulty.lower().startswith('e'):
            difficulty = 'easy'
            secretAnswer = random.randint(1, 10)
            maximumAnswer = 10
            maxGuessesAvailable = 4
            answerRange = '1 and 10'
            #return difficulty
            break
        elif difficulty.lower().startswith('m'):
            difficulty = 'medium'
            secretAnswer = random.randint(1, 30)
            maximumAnswer = 30
            maxGuessesAvailable = 5
            answerRange = '1 and 30'
            #return difficulty
            break          
        elif difficulty.lower().startswith('h'):
            difficulty = 'hard'
            secretAnswer = random.randint(1, 50)
            maximumAnswer = 30
            maxGuessesAvailable = 4
            answerRange = '1 and 50'
            #return difficulty
            break
        #if the player didn't type a difficulty mode i.e. '123$%' or 'George W. Bush'    
        #it makes the player enter type again until they enter a proper answer        
        else:
            print()
            print('''
                Please Enter proper answer:
                e for 'Easy' 
                m for 'Medium' 
                h for 'Hard'
                ''')     
    
    return difficulty, secretAnswer, maximumAnswer, maxGuessesAvailable, answerRange

#displays chosen difficulty
#I'm using the format() function to display the variables in a multi line
def displayAllStats(difficulty, maximumAnswer, maxGuessesAvailable):
    print('''
        ------------------------
         Difficulty = {diffHere}
        ------------------------
         Minimum Answer = 1
        ------------------------
         Maximum Answer = {maxAnswerHere}
        ------------------------
         Maximum Guesses = {maxGuessesAvailableHere}
        ------------------------

        '''.format(diffHere = difficulty, maxAnswerHere = maximumAnswer, maxGuessesAvailableHere = maxGuessesAvailable))

           
def gameIntro(answerRange):
    
    print('''Hi root,  
    I'm thinking of a number between {answerRangeHere} 

    '''.format(answerRangeHere = answerRange))

def getGuess(minimumAnswer, maximumAnswer):
    # This function returns the number the player entered 
    # P.S this function bugs out if the player entered a letter or a symbol i.e. 'Leet 'Lil Bitch' or '$$$'
    #//Holy fuck I fixed it
    
    # Holy fuck the game breaks 
    # if I answer
    # any and all numbers with operators like 1 + 1
    # fuck, and also any and all answers beginning with numbers and then symbols like '1 P' or '1@' or '1 $'
   
    while True:                                              
        print('====== ====== ======')
        print('  Your guess here:')
        print('====== ====== ======')
        print('         ,end = ''')
        print('====== ====== ======')
        guess = input()
        #makes sure player entered a number
        guessIsAllNumber = False
        for i in range(len(guess)): #checks if guess is all numbers

            if guess[i] in '0123456789': #if every character in guess is a number -> guessIsAllNumber is True
                guessIsAllNumber = True

            else:
                guessIsAllNumber = False #if not... the player is prompted to make a correct answer--one with just numbers in it

        if guessIsAllNumber: #if guessIsAllNumber is True -> it checks if player entered a number too low/too high(like -24 or 1000)
            guess = int(guess)

            if guess < minimumAnswer:
                print('----  ----  ----  ----  ----  ----  ----  ----')
                print(' The minimum number you can answer is ' + str(minimumAnswer) + '!')
                print('----  ----  ----  ----  ----  ----  ----  ----')

            elif guess > maximumAnswer:
                print('----  ----  ----  ----  ----  ----  ----  ----')
                print(' The maximum number you can answer is ' + str(maximumAnswer) + '!')
                print('----  ----  ----  ----  ----  ----  ----  ----')

            else:
                return guess #returns if there's nothing wrong with the guess

        else:
            print('''
                ------- ------ ------ ------
                 Please only enter NUMBERS
                 No special characters i.e
                 ($ / % / * / Q / @ / + / &)
                ------- ------ ------ ------
                ''')
   
def checkGuess(guess, secretAnswer):
    
    if guess < secretAnswer:
            print('''
                ------ ------ ------ ------
                   Your guess is too low
                ------ ------ ------ ------
                ''')
        
    elif guess > secretAnswer:
            print('''
                ------ ------ ------ ------
                   Your guess is too high
                ------ ------ ------ ------
                ''')

def confirmAnswer(guessesTaken):
    dash = '-' * len(playerName)
    if guess == secretAnswer:        
        print(''' 
        ##### ##### ##### #####
             You Won $$$
        You guessed the number
            in {guessTakenHere} guess(es)
        ##### ##### ##### #####
           Score:999999999
        ##### ##### ##### #####
            '''.format(guessesTakenHere = guessesTaken))

    elif guess != secretAnswer:
        print(''' 
        ===== ===== ===== =====
             You Lost ---
         The number that I was 
          thinking of was {secretAnswerHere}
        ===== ===== ===== =====
           Score:159124124
        ===== ===== ===== =====
            '''.format(secretAnswerHere = secretAnswer))

def playAgain():
    # Asks if player wants to play again
    print(''' 
    ------ ------ ------ ------
     Do you want to Play Again
             Yes | No
    ------ ------ ------ ------''')
    print('            ', end = '')
    return input().lower().startswith('y')
    print('------ ------ ------ ------')
    
def welcomeBackPlayer():
    dash = '-' 
    #Adds dash to the ASCII art depending on the length of the player name
    print('-----------------' + dash * len(playerName))
    print('-Welcome Back, ' + playerName + ' -')
    print('-----------------' + dash * len(playerName))	     
    print()
    print('Again, I am thinking of a number between ' + answerRange + '')

               
guessesTaken = 0
difficulty, secretAnswer, maximumAnswer, maxGuessesAvailable, answerRange = chooseDifficulty()
displayAllStats(difficulty, maximumAnswer, maxGuessesAvailable)
gameIntro(answerRange)
gameIsDone = False #set gameIsDone to False so it loops until player wins/loses
while True:

    while guessesTaken < maxGuessesAvailable:
        
        guess = getGuess(minimumAnswer, maximumAnswer)
        
        #adds 1 everytime player takes a valid guess              
        guessesTaken = guessesTaken + 1

        checkGuess(guess, secretAnswer)
        
        if guess == secretAnswer:
            break            

    gameIsDone = True
        
    # Ask the player if they want to play again (but only if the game is done
    if gameIsDone:
        confirmAnswer(guessesTaken) 

        if playAgain(): 
            guessesTaken = 0 
            difficulty, secretAnswer, maximumAnswer, maxGuessesAvailable, answerRange = chooseDifficulty()
            displayAllStats(difficulty, maximumAnswer, maxGuessesAvailable)     
            gameIntro(answerRange)  
            gameIsDone = False 
        else: 
            break

print('''
====== ===== ======
     Game Over
====== ===== ======
 Player: Anonymous
====== ===== ======
 Score:9999999999
====== ===== ======
''')
input()