#-*-coding:utf8;-*-
#qpy:3
#qpy:console

# Author: Jared I. Raga ©2018
# Email: jir@gmail.com
# Beginning  Date: 6/1/18
# Completion Date: 6/1/18 8:50PM
# Program Name: Fizz Buzz

#6/1/18 8:50PM

def getUserRange():
    while True:
        print('How many numbers to FizzBuzz')

        assignedRange = input('>')
        
        for number in assignedRange:
            if number not in '1 2 3 4 5 6 7 8 9 0'.split():                
                print('Please only enter numbers')
                break
        else:
            return assignedRange    

while True:
    maxNumber = getUserRange()
    
    for i in range(1, int(maxNumber) + 1):
        if i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)     


