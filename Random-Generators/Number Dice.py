#This code chooses a random number between your 2 provided numbers

# Author: Jared I. Raga ©2018
# Email: jir@gmail.com
# Beginning  Date: 5/28/18 
# Completion Date: 5/28/18
# Program Name: 'Assigned Number' Dice

#Made on:
#5/28/18

from random import randint


def getInput(start, end):
    while True:
        start = input('Specify Starting Number: ')
        
        if len(start) < 1:
            print('Please specify a number')
            print()
        
        for character in start:
            if character not in '1234567890':
                print('Please only input NUMBERS')
                print()
        else:
            break
    while True:
        end = input('Ending Number: ')
        
        if len(end) < 1:
            print('Please specify a number')
        for character in end:
            if character not in '1234567890':
                print('Please only input numbers')
        else:
            return start, end     
                       

print("'Random Number Chooser'")

startingNumber = ''
endingNumber = ''

while True:
    print()
    print()
    
    startingNumber, endingNumber = getInput(startingNumber, endingNumber)
    
    chooseRandom = randint(int(startingNumber), int(endingNumber))
    
    print()
    print('Chosen Number: |' + str(chooseRandom) + '|')