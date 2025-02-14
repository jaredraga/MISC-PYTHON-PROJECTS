#testing Random Number Generator
#announces if a number was repeated

#flow chart
#produce 10,000 random numbers
#check if a number has been repeated
#end/play again

#success 5/12/18 12:55AM

import random

def getRandom():
	number = random.randint(1, MAXNUMBER)
	print(number)

	return number

def checkingNumbers():
    print('Task finished')
    print('Check the numbers? [y/n]')	
    checkNumbers = input()
	
    if checkNumbers.lower().startswith('y'):
           
        cycle = 0 #records how many checks the user made
        while True:
            cycle = cycle + 1
            checking = input()   
            
            if cycle == 2:
                print('Type \'x\' to stop')                            
            if checking == 'x':
                break
            elif checking in numbersAlreadyPrinted:
                print(checking + ' detected!')
            else:
                print(checking + ' was not detected.')
            cycle = cycle + 1
	
    gameIsDone = True
    return gameIsDone
	 
def playAgain():
	print('Do you want to play again? [y/n]')
	return input().lower().startswith('y')

MAXNUMBER = 1000000000000000000000000000000000000 #change this variable value if you want to change the max number
	
numbersAlreadyPrinted = []
cycle = 0
gameIsDone = False
while cycle <= MAXNUMBER:
	randomNumber = getRandom()
	cycle = cycle + 1
	if str(randomNumber) in numbersAlreadyPrinted:	
		print('Repetition Detected!: ' + str(randomNumber))
		print('Cycles: '+ str(cycle) + '/' + str(MAXNUMBER))
		print()
		gameIsDone = True
	else:
		numbersAlreadyPrinted = numbersAlreadyPrinted + [str(randomNumber)]
	
	if cycle == MAXNUMBER:	
		checkingNumbers()

	if gameIsDone == True:
		if playAgain(): #checks if play again is True
			numbersAlreadyPrinted = []
			cycle = 0
			gameIsDone = False			

		else:
			break


