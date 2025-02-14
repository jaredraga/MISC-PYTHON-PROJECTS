#Making the hangman game
#started:
#5/30/18

#Come up with secret word
#Make player guess word
#letter not in word | letter in word
#player wins | player loses
#play again | end

#5/30/18
#its not working
#lol wtf is happening

#6/1/18 
#it's fixed
#and it's finished

import random

HANGMANPICS = ['''   
             +---+ 
             |   | 
                 | 
                 | 
                 | 
                 | 
           =========''', ''' 
  
             +---+ 
             |   | 
             O   | 
                 | 
                 | 
                 | 
           =========''', ''' 
  
             +---+ 
             |   | 
             O   | 
             |   | 
                 | 
                 | 
           =========''', ''' 
  
             +---+ 
             |   | 
             O   | 
            /|   | 
                 | 
                 | 
           =========''', ''' 
 
             +---+ 
             |   | 
             O   | 
            /|\  | 
                 | 
                 | 
           =========''', ''' 
  
             +---+ 
             |   | 
             O   | 
            /|\  | 
            /    | 
                 | 
           =========''', ''' 
  
             +---+ 
             |   | 
             O   | 
            /|\  | 
            / \  | 
                 | 
           =========''','''
           
             +---+ 
             |   | 
            [O   | 
            /|\  | 
            / \  | 
                 | 
           =========''',''' 
           
             +---+ 
             |   | 
            [O]  | 
            /|\  | 
            / \  | 
                 | 
           =========''','''
           
             +---+ 
             |   | 
            [O]  | 
            /|\  | 
            /'\  | 
                 | 
           =========''']                            
                      

words = {'colors':'blue red green'.split(), 'animals':'dog cat mouse'.split(), 'foods':'ham bacon egg'.split()} 

#words = 'ham bacon egg'.split()

def getRandomWord(words):
    
    wordKey = random.choice(list(words.keys()))
    wordIndex = random.randint(0, len(words) - 1)
    
    return words[wordKey][wordIndex], wordKey

def displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord):    
    print(HANGMANPICS[len(missedLetters)])
    print()
    
    print('Missed Letters:', end = ' ')
    for letter in missedLetters:
        print(letter, end = ' ')
    print()
    
    blanks = '_' * len(secretWord)
    
    for i in range(len(secretWord)):
    	    if secretWord[i] in correctLetters:
    	        blanks = blanks[:i] + secretWord[i] + blanks[i+1:]
    	        
    for letter in blanks:
    	    
    	    print(letter, end = ' ')
    	
    print()          
    	
def getGuess(alreadyGuessed):
    while True:
        #print('Category: ' + secretWord[1])
        print()
        print('Guess a letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please only enter a SINGLE letter.')
        elif guess in alreadyGuessed:
            print('You already guessed that letter.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please only enter LETTERS.')
        else:
            return guess    

def playAgain():
    print('Do you want to play again?')
    
    return input().lower().startswith('y')
            	           
print(' H A N G M A N ') 
print()
 
missedLetters = '' 
correctLetters = ''
secretWord, secretKey = getRandomWord(words)

gameIsDone = False

while True:
    print('The secret word is in the set: ' + secretKey)
    displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
    
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess
        
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
       
        if foundAllLetters:
            displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
            print()
            print('Congratulations, you guessed it correctly the secret word is "'+ secretWord +'"! You have won!')
            gameIsDone = True
            
    else:
        missedLetters = missedLetters + guess   
        
        if len(missedLetters) == len(HANGMANPICS) - 1:
            displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
            print()
            print('You have ran out of guesses. The secret word was "'+ secretWord +'" ')
            gameIsDone = True    
                  
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord, secretKey = getRandomWord(words)       
        else:
            break           
        