#Guess The Number Game
#from scratch
#by duck (:

import random
import time

def gameIntro():
    print('Blah ')
    time.sleep(2)
    print('Blah Blah ')
    time.sleep(2)
    print('Blah Blah Blah ')
    time.sleep(2)
    
def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print('(1/2)? ')
        cave = input()
    
    return cave

    
def checkCave(chosenCave):
    print('Blah ')
    time.sleep(2)
    print('Blah Blah Blah ')
    time.sleep(2)
    
    friendlyCave = random.randint(1, 2)
    
    if chosenCave == str(friendlyCave):
        print('Win!')
        
    else:
        print('Lose.')
    
    
playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':       

    gameIntro()
    
    caveNumber = chooseCave()
    
    checkCave(caveNumber)   
    
    print('Play Again? (yes/no)')
    playAgain = input()