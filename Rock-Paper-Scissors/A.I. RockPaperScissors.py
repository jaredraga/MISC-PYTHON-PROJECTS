#-*-coding:utf8;-*-
#qpy:3
#qpy:console

# Author: Jared I. Raga ©2018
# Email: jir@gmail.com
# Beginning  Date: 5/30/18
# Completion Date: 5/31/18 1:10AM
# Program Name: A.I. RockPaperScissors

print("This is console module")

#started
#5/30/18
#finished
#5/31/18 1:10AM

from random import randint
from time import sleep

playableHands = ['Rock', 'Paper', 'Scissors']


#Lin Fans Alex and Lin Fan

def conclusion(alex, linFan):  
    #spaces = ' ' * (23 - len(alex + linFan))
          
    #if the two guys have the same hand, it's a draw
    if alex == linFan:                
        win = 'draw'    
        
    if alex == 'Rock' and linFan == 'Scissors':               
        win = 'alex'
        
    elif alex == 'Rock' and linFan == 'Paper':        
        win = 'linFan'
    
    if alex == 'Paper' and linFan == 'Rock':        
        win = 'alex'
        
    elif alex == 'Paper' and linFan == 'Scissors':        
        win = 'linFan'
        
    if alex == 'Scissors' and linFan == 'Paper':        
        win = 'alex' 
        
    elif alex == 'Scissors' and linFan == 'Rock':        
        win = 'linFan'
   
   
    if win == 'draw':
        symbol = '='
    elif win == 'alex':
        symbol = '<'
    elif win == 'linFan':
        symbol = '>'
        
    leftSpace = ' ' * (11 - len(alex))
    rightSpace = ' ' * (11 - len(linFan))
    #print('Alex:'+ alex + leftSpace + symbol + rightSpace + linFan + ':Lin Fan') 
                     
    return win   
 
def score(alex, linFan, draws):
    
    if win == 'draw':
        draws = draws + 1
    
    if win == 'alex':
        alex = alex + 1
            
    elif win == 'linFan':
        linFan = linFan + 1
        
    return alex, linFan, draws 
  
alexScore = 0
linFanScore = 0
draws = 0
rockPlayed = 0
paperPlayed = 0
scissorsPlayed = 0

turns = 0
gamesPlayed = 0


while True:
    if turns == 10:
        spaces = ' ' * (15 - len(str(alexScore))) 
        print(spaces + str(alexScore) + ' | ' + str(linFanScore))     
   
        spaces = ' ' * 12       
        print(spaces + 'Draw:' + str(draws))
        print(gamesPlayed)
        print('Rocks:' +str(rockPlayed))
        print('Papers:' +str(paperPlayed))
        print('Scissors:' +str(scissorsPlayed))
        print()
        turns = 0                    
                       
    alexChoice = randint(0, len(playableHands) -1)
    alexHand = playableHands[alexChoice]
    
    linFanChoice = randint(0, len(playableHands) -1)
    linFanHand = playableHands[linFanChoice]

    if alexHand == 'Rock':
        rockPlayed = rockPlayed + 1
    if alexHand == 'Paper':
        paperPlayed = paperPlayed + 1
    if alexHand == 'Scissors':
        scissorsPlayed = scissorsPlayed + 1
   
    if linFanHand == 'Rock':
        rockPlayed = rockPlayed + 1
    if linFanHand == 'Paper':
        paperPlayed = paperPlayed + 1
    if linFanHand == 'Scissors':
        scissorsPlayed = scissorsPlayed + 1
               
    win = conclusion(alexHand, linFanHand)
    alexScore, linFanScore, draws = score(alexScore, linFanScore, draws)
    
    turns = turns + 1
    gamesPlayed = gamesPlayed + 1
    
    sleep(0.000001)
    