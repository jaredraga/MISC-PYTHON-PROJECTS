
#5/29/18

from random import randint

playableHands = ['Rock', 'Paper', 'Scissors']


def getPlayerHand(choices):
    playerHand = ''
    while playerHand not in choices:
        playerHand = input()
        
        if playerHand not in choices:
            print()
            print('Please choose from Rock, Paper or Scissors \n')

    return playerHand

def conclusion(computer, player):
    print()
    #if the two guys have the same hand, it's a draw
    if computer == player:
        print('The computer played ' + computer + '.')
        print('Draw!')
        
        win = 'draw'    
        
    if computer == 'Rock' and player == 'Scissors':
        print('The computer played ' + computer + '.')
        print('Computer wins!')
        
        win = 'computer'
        
    elif computer == 'Rock' and player == 'Paper':
        print('The computer played ' + computer + '.')    
        print('Player wins!')
        
        win = 'player'
    
    if computer == 'Paper' and player == 'Rock':
        print('The computer played ' + computer + '.')
        print('Computer wins!')
        
        win = 'computer'
        
    elif computer == 'Paper' and player == 'Scissors':
        print('The computer played ' + computer + '.')
        print('Player wins!')
        
        win = 'player'
        
    if computer == 'Scissors' and player == 'Paper':
        print('The computer played ' + computer + '.')
        print('Computer wins!')
        
        win = 'computer' 
        
    elif computer == 'Scissors' and player == 'Rock':
        print('The computer played ' + computer + '.')
        print('Player wins!')
        
        win = 'player'
        
    return win   
 
def score(computer, player):
    
    if win == 'computer':
        computer = computer + 1
            
    elif win == 'player':
        player = player + 1
        
    return computer, player   
  
computerScore = 0
playerScore = 0

while True:
    print('\n')
    print('Computer: ' + str(computerScore))
    print('Player  : ' + str(playerScore))  
    print('\n')      
    print('What\'s your hand choice:')
    print('Rock, Paper, or Scissors?')
    print()
    
        
    computerChoice = randint(0, len(playableHands) -1)
    computerHand = playableHands[computerChoice]
    playerHand = getPlayerHand(playableHands)


    win = conclusion(computerHand, playerHand)
    computerScore, playerScore = score(computerScore, playerScore)