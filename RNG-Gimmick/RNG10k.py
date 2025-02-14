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
	print('Check the numbers?')
	checking = input()
	if checking in numbersAlreadyPrinted:
		print(checking + ' detected!')
	else:
	 	print(checking + ' was not detected.')

def playAgain():
	print('Do you want to play again? [y/n]')
	return input().lower().startswith('y')

MAXNUMBER = 10000 #change this variable value if you want to change the max number
	
numbersAlreadyPrinted = []
cycle = 0
gameIsDone = False
while cycle < MAXNUMBER:
	randomNumber = getRandom()

	if str(randomNumber) in numbersAlreadyPrinted:	
		print('Repetition Detected!: ' + str(randomNumber))
		print('Cycles: '+ str(cycle) + '/' + str(MAXNUMBER))
		gameIsDone = True
	else:
		numbersAlreadyPrinted = numbersAlreadyPrinted + [str(randomNumber)]
	
	if cycle == MAXNUMBER:	
		checkingNumbers()
		if playAgain():
			gameIsDone == True

	if gameIsDone == True:
		if playAgain():
			numbersAlreadyPrinted = []
			cycle = 0
			gameIsDone = False			

	cycle = cycle + 1


