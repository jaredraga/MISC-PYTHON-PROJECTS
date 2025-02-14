#Testing Return Values

import random

#creates function 'testNumber():
def testNumber():
    #creates variable 'number'. 'random.randint()' function produces a random number depending on the perimeter. e.g. (1, 20) produces random number between 1 and 20
    number = random.randint(999999, 1000000)
    
    #exits the def function with the 'number' variable's value recorded for later use.
    return number

#creates function 'printNumber' with perimeter (chosenNumber)
def printNumber(chosenNumber):
    #prints the value of the variable 'number'
    print(numberTest)

#creates while loop that; while value of playAgain is equal to 'yes' or 'y' the loop plays again
playAgain = 'yes'  
while playAgain == 'yes' or playAgain == 'y':
    
    
    numberTest = testNumber()
    
    printNumber(numberTest)

    print('Play Again? (yes/no)')
    playAgain = input()

#success! -canard (: