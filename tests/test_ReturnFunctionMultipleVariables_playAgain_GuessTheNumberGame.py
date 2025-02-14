import random

def testNameFunction():
    print('Type your name')
    name = input()

    return name
    
def testPassFunction():

    print('Print your password')
    password = input()

    return password

def printVars():
    print('Name: ' + str(playerName) + ' ')
    print('Password: ' + str(playerPass) + ' ') 
        
    return
    
playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':       
    
    playerName = testNameFunction()
    
    playerPass = testPassFunction()       
    
    printVars()

    print('Play Again? (y/n)')
    playAgain = input()

#success! -duck
