#Started on
#6/24/18 7:30AM

import random
import sys
import time
import tictactoe

# Make:
# Be able to choose other games from the main menu.

# Change guest highscore to 0 everytime the game exits.
# Make a main Menu site that could be accessed with the type of a button from anywhere
# Main menu site contains:
# Hall Of Fame
# Login
# Register
# Games

#Make:
#Seperate scoring system
#Own stats viewer
#Pass username to the games
#Do scoring system for tictactoe

#Have:
#Consequences for games
#If lost for an amount of times;
#He/She loses.

#TicTacToe is counted on how much you win 
#in a single game without losing
#Make:
#Scoring clear

#Apply:
#Pauses between computer turns
#It feels more human and fair

#Bug:
#There are bugs.

#Edit:
#Don't remove the guest account every time
#Just turn its score to 0 everytime they exit
#Record draws on easy tic tac toe
#Do the scoring rules later

#I:
#Wiped my progress
#Redo it with the game's scoring system
#and Fixing the Guest Bug by not removing but instead rewriting
#and separating the isNewHighscore() from the updateScore()

# Started Editing on Computer on: 7/20/18 1:25AM

def hallOfFame():       
       
    with open("accounts.txt","r") as f: 
        data = f.readlines()        
        sortedData = sorted(data, key=lambda item: int(item.split()[1]), reverse=True)
        top = sortedData[:10]
        number = 1
        print('~ ~ ~ HALL OF FAME ~ ~ ~')
        for user in top:
            stats = user.split()
            print(str(number) + '.' + ' ' * (2 - len(str(number))) + stats[0] + ' ' * ((13 - len(stats[0]))) + stats[1])
            number += 1
        print()
        print('       BACK(Any Key)')
        input()
        
def fakeLoadingBar():    
        
    for i in range(101):    
               
        t = random.uniform(.01, .02)
        
        time.sleep(t)     
        sys.stdout.write("\r%d%%" % i) 
        sys.stdout.flush()
    print(' Finished Loading')
    
def isAnExistingAccount(username):
    with open("accounts.txt","r") as f: 
        data = f.readlines()             
        for line in data:
            usersData = line.split()       
            existingUsername = usersData[0]           
            if str(username) == str(existingUsername):
                return True
                
def isUsernameValid(username):
    #If over ten character limit
    if len(username) > 10:
        print('Sorry, Over 10* character limit.')
        return False
    
    if len(username) < 2:
        print('Sorry, Less than two characters.')
        return False
        
    #If there are spaces and invalid characters
    for i in username:
        if not i.isalpha() or i == ' ':
            print('Sorry, Contains invalid characters!')
            return False
    
    #If username is already in use        
    if isAnExistingAccount(username): 
        print('Sorry, Username already in use!')
        return False
     
    # Return True if nothing is violated           
    return True       

def displayStats(currentUsername):
    with open("accounts.txt","r") as f: 
        data = f.readlines()             
        for line in data:
            userData = line.split()                             
            if str(currentUsername) == str(userData[0]):
                print('User: ' + userData[0] + ' ' * ((11 - len(userData[0]))) + 'Highscore:' + userData[1])
    time.sleep(3)
    
def playAccount():
    
    print('Hello! Welcome!')
    print("•If you don't have an account yet, type 'A' to create a new account")   
    print()
    print("•If you don't want to login, type 'G' to play as guest")
    print()
    print('•If not:')
    
    while True:               
        print('Login in with your account here:')
        username =	input('>')
        
        if username.upper() == 'A':
            return 'A'
        if username.upper() == 'G':
            return 'G'
        if isAnExistingAccount(username):
            print('Welcome, '+ username + '!')
            print()
            print("Loading user data...")
            fakeLoadingBar()
            print()            
            displayStats(username)
            
            return username
        
        
               
    print('Sorry, you have failed to enter the correct username.')          
    return None
            
# Adding a new account
def addNewAcc():
    print('Creating New Username')
    print()
    print('Hello! Welcome!')
    print()
    print('Here are some rules in creating a new username:')
    print('•Up to 10 characters only*')
    print('•No less than two characters')
    print('•No spaces')
    print('•Only words and letters')
    print()
    print()
    while True:
        print("Hello! Please add your username!")
        username = input('>')
        
        if isUsernameValid(username):
            with open("accounts.txt", "a") as f: 
                f.write('\n')
                f.write(username + " 0")

            print('Welcome, '+ username +'! Your account was succesfully created!')
            print("Loading user data...")
            fakeLoadingBar()
            displayStats(username)
            
            return username
                        
        print()        
        print()
                

def isNewHighscore(currentScore, username):
    # Check if current score is greater than previous highscore
    with open("accounts.txt",'r') as f: 
        data = f.readlines()
        for line in data:
            userData = line.split()
            if username == userData[0]:
                if int(currentScore) > int(userData[1]):
                    return True
                # return false if the current score is not greater than highscore
                else:               
                    return False

def updateScore(currentScore, username):        
    # UPDATING USER HIGHSCORE         
    
    with open("accounts.txt","r") as f:
        data = f.readlines()
    
    # Change the highscore of the user if new highscore
    with open("accounts.txt",'w') as f: 
        for line in data: ## STARTS THE NUMBERING FROM 1 (by default it begins with 0) 
            userData = line.split()
            if username == userData[0]: ## OVERWRITES line:2                         
                f.writelines(username + ' ' + str(currentScore) + '\n')                              
            else: 
                f.writelines(line)

def loginAsGuest():
    #print('Logging in with a guest account...')
    #print("Are you sure? Your score won't be recorded. (type almost any button to proceed)")
    #print()
    #print("Type 'L' to login to your account")
    #print("Type 'A' to create new username")
    #print()
    #letter = input()
    #if letter.upper() == 'L':
        #username = playAccount()
    #elif letter.upper() == 'A':
    #        username = addNewAcc() 
    
    
    #with open("accounts.txt", "a") as f:        
        #f.write('\n')
        #f.write('Guest' + " 0")    
    
    return 'Guest'

def resetGuestAccount():
    # Store the contents in a variable
    with open("accounts.txt",'r') as f: 
        data = f.readlines()
    
    # Reseting the guest account 
    with open("accounts.txt",'w') as f: 
        for line in data: ## STARTS THE NUMBERING FROM 1 (by default it begins with 0) 
            userData = line.split()
            if 'Guest' == userData[0]: ## OVERWRITES line:2                         
                f.writelines('Guest 0')         
            else:
                f.writelines(line)
                
    # Remove blank lines
    #with open('testAccounts.txt') as f: 
    #    lines = f.readlines() 

    #with open('testAccounts.txt', 'w') as f: 
    #    lines = filter(lambda x: x.strip(), lines) 
    #    f.writelines(lines)                              

def login():
    username = playAccount()

    if username == 'A':    
        username = addNewAcc()    

    elif username == 'G':
        username = loginAsGuest()

    return username

def confirmExit():
    print('Confirm Save & Exit? (y/n)')
    return input().lower().startswith('y')







# UNBEATABLE TIC TAC TOE ↓↓↓↓
    
def unbeatableTicTacToe(username):
    print('Welcome to Unbeatable Tic Tac Toe!')
    
    playerScore = 0
    computerScore = 0
    draws = 0
    while True:
        print('Score:')
        print('    '+username+':' + str(playerScore))
        print('    Computer:' + str(computerScore))
        print('    Draws:' + str(draws))
        theBoard = [' '] * 10
        playerLetter, computerLetter = ['X','O'] #inputPlayerLetter()
        turn = tictactoe.whoGoesFirst()
        firstMove = turn
        print('The ' + turn + ' will go first.')
        gameIsPlaying = True
        moveInTheMiddleForTie = True
        
        while gameIsPlaying:
            if turn == 'player':
                tictactoe.drawBoard(theBoard)
                move = tictactoe.getPlayerMove(theBoard)
                tictactoe.makeMove(theBoard, playerLetter, move)
    
                if tictactoe.isWinner(theBoard, playerLetter):
                    tictactoe.drawBoard(theBoard)
                    print('Hooray, you have won the game!')
                    playerScore += 1
                    gameIsPlaying = False
                else:
                    if tictactoe.isBoardFull(theBoard):
                        tictactoe.drawBoard(theBoard)
                        print('The Game is a Tie')
                        draws += 1
                        break
                    else:
                        turn = 'computer'
            else:
                # Computer's Turn
    
                # Move to the middle if the first move is the player
                if firstMove == 'player':# and isSpaceFree(theBoard, 5) and moveInTheMiddleForTie:
                    move = tictactoe.moveAgainstPlayer(theBoard, computerLetter)
                    tictactoe.makeMove(theBoard, computerLetter, move)
                    moveInTheMiddleForTie = False
                else: # If first move is the computer
                    move = tictactoe.getComputerMove(theBoard, computerLetter)
                    tictactoe.makeMove(theBoard, computerLetter, move)
    
                if tictactoe.isWinner(theBoard, computerLetter):
                    tictactoe.drawBoard(theBoard)
                    print('The computer has won.')
                    computerScore += 1
                    gameIsPlaying = False
    
                else:
                    if tictactoe.isBoardFull(theBoard):
                        tictactoe.drawBoard(theBoard)
                        print('The Game is a Tie')
                        draws += 1
                        break
                    else:
                        turn = 'player'
    
        #if tictactoe.playAgain() == False:
        #return playerScore
            #break
    
    return (playerScore * 1000)
# UNBEATABLE TIC TAC TOE ↑↑↑↑↑↑



# EASY TIC TAC TOE ↓↓↓↓↓↓
# Just borrowing the functions from the unbeatable
# There's no difference anyways, just added some function in the unbeatable            
def easyTicTacToe(username):
    time.sleep(1)
    print('Welcome to Easy Tic Tac Toe!')    
    playerScore = 0
    computerScore = 0 
    draws = 0
    while True:
        theBoard = [' '] * 10
        playerLetter, computerLetter = ['X','O']#inputPlayerLetter()       
        turn = tictactoe.whoGoesFirst()
        #time.sleep(1)
        print('Score:')
        print('    '+username+':' + str(playerScore))
        print('    Computer:' + str(computerScore))
        #time.sleep(1)
        print('The ' + turn + ' will go first.')
        gameIsPlaying = True
        #time.sleep(1)
        while gameIsPlaying:
            if turn == 'player':                 
                tictactoe.drawBoard(theBoard)
                move = tictactoe.getPlayerMove(theBoard)
                tictactoe.makeMove(theBoard, playerLetter, move)
            
                if tictactoe.isWinner(theBoard, playerLetter):
                    tictactoe.drawBoard(theBoard)
                    print('Hooray! You have won the game.')            
                    playerScore += 1
                    gameIsPlaying = False
                else:
                    if tictactoe.isBoardFull(theBoard):
                        tictactoe.drawBoard(theBoard)
                        print('The game is a tie!')
                        draws += 1
                        break
                    else:
                        turn = 'computer'
            
                print()

            else:
                #t = random.randint(2,3)
                tictactoe.drawBoard(theBoard) 
                #time.sleep(t)                                                                   
                # Computer's turn.
                move = tictactoe.getComputerMove(theBoard, computerLetter)
                tictactoe.makeMove(theBoard, computerLetter, move)
                
                if tictactoe.isWinner(theBoard, computerLetter):
                    tictactoe.drawBoard(theBoard)                    
                    print('The computer has beaten you! You lose.')
                    computerScore += 1
                    gameIsPlaying = False
                else:
                    if tictactoe.isBoardFull(theBoard):
                        print('The game is a tie!')
                        draws += 1
                        break
                    else:
                        turn = 'player'
                
        #if not tictactoe.playAgain():
        #return playerScore
            #break
    
    return playerScore
# EASY TICTACTOE ↑↑↑↑

def tictactoeMainMenu():
    print('''~ ~ ~ TIC TAC TOE ~ ~ ~

Choose Mode:

1 - Easy
2 - Impossible
    ''')

    diff = ''
    while not (diff == '1' or diff == '2'):
        diff = input('Choose mode:')
    
    if diff == '1':
        return 'easy'
    if diff == '2':
        return 'unbeatable'    



def gameMenu(username):
    score = 0
    while True:   
        print('= = = = = GAMES = = = = =')
        print('Logged in as: ' + username)
        print()
        print('1. TicTacToe')   
        print()
        print('9. Back to Main Menu')
        wantToPlay = input('>')
        
        if wantToPlay == '1':
            tTTDiff = tictactoeMainMenu()
            if tTTDiff == 'easy':
                print('Loading TicTacToe: Easy Mode')
                fakeLoadingBar()
                time.sleep(1)
                score = score + easyTicTacToe(username)
            elif tTTDiff == 'unbeatable':
                print('Loading TicTacToe: Unbeatable Mode')
                fakeLoadingBar()
                time.sleep(1)
                score = score + unbeatableTicTacToe(username)
        
        # backdoor: score hack
        elif wantToPlay == '@@@':          
            cycle = 0
            
            while True:
                print(cycle)
                scoreToAdd = input("Score to add('done' to exit): ") 
                
                cheatInvalid = False
                for i in scoreToAdd:
                    if i not in '123456790':
                        print('Numbers only ' + i)
                        cheatInvalid = True


                if scoreToAdd == 'done':
                    break
               
                if cheatInvalid == False:    
                    score += int(scoreToAdd)
                    updateScore(score, username)                
                        
                cycle += 1
                
            print('ALERT: Someone used the backdoor')
        
        #if user gets new highscore, update it.
        if isNewHighscore(score, username):
            updateScore(score, username)
       
        if wantToPlay == '9':
            break
            
        
        
    return score
    
def accountStats(currentUsername):
    with open("accounts.txt","r") as f: 
        data = f.readlines()             
        for line in data:
            userData = line.split()                             
            if str(currentUsername) == str(userData[0]):
                print('- - - - ACCOUNT - - - -')             
                print(' ' * (12 - int(len(userData[0])/2)) + userData[0])
                print()
                print('      Highscore:' + str(userData[1]))
                input()
                
def mainMenu():   
    username = loginAsGuest()
    while True:
        print('~ ~ ~ ~ MAIN__MENU ~ ~ ~ ~')
        print('         GAMES(1)')
        print()
        print('         LOGIN(2)')
        print()
        print('        REGISTER(3)')
        print()
        print('        ACCOUNT(4)')
        print()
        print('      HALL OF FAME(5)')
        print()
        print('         EXIT(9)')
        print()
        print('    (Logged in as ' + username + ')')
        print()          
        wantTo = input('>')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~')
        
        if wantTo == '1':
            score = gameMenu(username)
        elif wantTo == '2':
            username = login()
        elif wantTo == '3':
            username = addNewAcc()       
        elif wantTo == '4':
            accountStats(username)
        elif wantTo == '5':
            hallOfFame()        
        elif wantTo == '9':
            if confirmExit():                
                return
            print('Cancelled Exit.')

if __name__ == '__main__':
    mainMenu()
    resetGuestAccount()
    print('Game Saved and Safely Exited')

