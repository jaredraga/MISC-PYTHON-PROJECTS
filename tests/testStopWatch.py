#Stopwatch 
#By -Duck (:
#4/24/18

#Flow Chart:
# Ask how long they want before timeout
# Start
# Stop

import time

SPACES = ['''








































               
                ''']
                
print('Time(seconds):', end=' ')

userInput = input()
userInput = int(userInput)

seconds = 0
MINUTES = 60
HOURS = MINUTES * 60
DAYS = HOURS * 24
MONTHS = DAYS * 31
while True:
    timeLeftSecs = userInput  - seconds
    timeLeftMins = int(timeLeftSecs/MINUTES)
    print(SPACES[0])
    if timeLeftSecs < MINUTES:   
        print('Time Left: 0 minute and ' + str(timeLeftSecs) + ' ', end='')
        if timeLeftSecs <= 1:
            print('second')
        else:
            print('seconds')
    if timeLeftSecs >= MINUTES:
        print('Time Left:' + str(timeLeftMins) + ' ',end='')
        if timeLeftMins <= 1:
            print('minute ',end='')
        else:
            print('minutes ', end='')
        print('and ' + str(timeLeftSecs - MINUTES) + ' ', end='')
        if timeLeftSecs <= 1:
            print('second')
        else:
            print('seconds')
     
    # if timeLeftSecs >= HOURS:
               
    time.sleep(1)
    
    seconds = seconds + 1 
    
    if timeLeftSecs == 0:
        break

print()
print('         |Your time is up|')
input()