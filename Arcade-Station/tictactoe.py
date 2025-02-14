import random
import time

def main():
    print('Welcome to Unbeatable Tic Tac Toe!')
    
    playerScore = 0
    computerScore = 0
    draws = 0
    while True:
        print('Score:')
        print('    Player:' + str(playerScore))
        print('    Computer:' + str(computerScore))
        print('    Draws:' + str(draws))
        theBoard = [' '] * 10
        playerLetter, computerLetter = ['X','O'] #inputPlayerLetter()
        turn = whoGoesFirst()
        firstMove = turn
        print('The ' + turn + ' will go first.')
        gameIsPlaying = True
        moveInTheMiddleForTie = True
        
        while gameIsPlaying:
            if turn == 'player':
                drawBoard(theBoard)
                move = getPlayerMove(theBoard)
                makeMove(theBoard, playerLetter, move)
    
                if isWinner(theBoard, playerLetter):
                    drawBoard(theBoard)
                    print('Hooray, you have won the game!')
                    playerScore += 1
                    gameIsPlaying = False
                else:
                    if isBoardFull(theBoard):
                        drawBoard(theBoard)
                        print('The Game is a Tie')
                        draws += 1
                        break
                    else:
                        turn = 'computer'
            else:
                # Computer's Turn
    
                # Move to the middle if the first move is the player
                if firstMove == 'player':# and isSpaceFree(theBoard, 5) and moveInTheMiddleForTie:
                    move = moveAgainstPlayer(theBoard, computerLetter)
                    makeMove(theBoard, computerLetter, move)
                    moveInTheMiddleForTie = False
                else: # If first move is the computer
                    move = getComputerMove(theBoard, computerLetter)
                    makeMove(theBoard, computerLetter, move)
    
                if isWinner(theBoard, computerLetter):
                    drawBoard(theBoard)
                    print('The computer has won.')
                    computerScore += 1
                    gameIsPlaying = False
    
                else:
                    if isBoardFull(theBoard):
                        drawBoard(theBoard)
                        print('The Game is a Tie')
                        draws += 1
                        break
                    else:
                        turn = 'player'
    
        #if playAgain() == False:
        playerScore *=  1000           
            #break
    
    return playerScore

def drawBoard(board):
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def inputPlayerLetter():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()

    if letter == 'X':
        return ['X','O']
    else:
        return ['O','X']

def whoGoesFirst():
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

def playAgain():
    print('Do you want to play again? (yes/no)')
    return input().upper().startswith('Y')

def makeMove(board, letter, move):
    board[move] = letter

def isWinner(bo, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or #across the top
        (bo[4] == le and bo[5] == le and bo[6] == le) or #across the middle
        (bo[1] == le and bo[2] == le and bo[3] == le) or #across the bottom
        (bo[7] == le and bo[4] == le and bo[1] == le) or #down the left
        (bo[8] == le and bo[5] == le and bo[2] == le) or #down the middle
        (bo[9] == le and bo[6] == le and bo[3] == le) or #down the right
        (bo[7] == le and bo[5] == le and bo[3] == le) or #diagonal
        (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal

def getBoardCopy(board):
    
    dupeBoard = []

    for i in board:
        dupeBoard.append(i)

    return dupeBoard

def isSpaceFree(board, move):
    return board[move] == ' '

def getPlayerMove(board):
    move = ' '
    while True:
        print('What is your next move? 1-9')
        move = input()

        if move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
            print('Invalid Move')
        else:
            break                  

    return int(move)

def chooseRandomMoveFromList(board, movesList):

    possibleMoves = []

    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def moveAgainstPlayer(board, computerLetter):
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    bo = board
    pL = playerLetter

    if isSpaceFree(board, 5):
        return 5

    # Check if he could win on his next move
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i

    # Check if the player could win on his next move and block it
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i

    if bo[1] and pL == bo[9] and pL or bo[7] and pL == bo[3] and pL:
        return chooseRandomMoveFromList(board, [2,4,6,8])

    # Try to take one of the corners, if it is a valid move.
    move = chooseRandomMoveFromList(board, [9,7,3,1])
    if move != None:
        return move

    # Try to take the center, if it is a valid move
    if isSpaceFree(board, 5):
        return 5

    # Take on of the sides if there's no other move
    return chooseRandomMoveFromList(board, [2,4,6,8])

def isNotOccupiedByPlayer(bo, pL, spacesList):
    
    for space in spacesList:
        if bo[space] == pL:
            return False
            
    return True
    
def winningMoveIfComputerGoesFirst(board, playerLetter):
    
    bo = board
    pL = playerLetter
    
    if pL == 'X':
        cL = 'O'
    else:
        cL = 'X'
        
    if isNotOccupiedByPlayer(board, playerLetter, [5,1,3,7,8]):
        if bo[2] == pL and bo[1] == cL or bo[3] == cL:
            return chooseRandomMoveFromList(bo, [7,9])
        
        elif bo[4] == pL and bo[1] == cL or bo[7] == cL:
            return chooseRandomMoveFromList(bo, [3,9])
        
        elif bo[6] == pL and bo[3] == cL or bo[9] == cL:
            return chooseRandomMoveFromList(bo, [1,7])
        
        elif bo[8] == pL and bo[7] == cL or bo[9] == cL:
            return chooseRandomMoveFromList(bo, [1,3])
                            
def getComputerMove(board, computerLetter):
    
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    # Check if he could win on his next move
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i

    # Check if the player could win on his next move and block it
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i

    #move = winningMoveIfComputerGoesFirst(board, playerLetter)
    #if move != None:
        #return move
    
    # Try to take one of the corners, if it is a valid move.
    move = chooseRandomMoveFromList(board, [9,7,3,1])
    if move != None:
        return move

    # Try to take the center, if it is a valid move
    if isSpaceFree(board, 5):
        return 5

    # Take on of the sides if there's no other move
    return chooseRandomMoveFromList(board, [2,4,6,8])

def isBoardFull(board):

    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False

    return True

if __name__ == '__main__':
    main()