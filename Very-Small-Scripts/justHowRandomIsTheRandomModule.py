import random, time

one = 0
two = 0
three = 0
four = 0
five = 0
six = 0

cycle = 0
iRise = True
iFall = False
howManyI = 1
letterRise = '-'
letterFall = '-'
	
while cycle < 1000:
    
    time.sleep(0.01)
    
    if iRise:
        print(letterRise * howManyI)
        howManyI += 1
        if howManyI == 36:
            iRise = False
            iFall = True
    
    if iFall:
        print(letterFall * howManyI)
        howManyI -= 1
        if howManyI == 1:
            iRise = True
            iFall = False       
    
    #time.sleep(0.05)
    randomNumber = random.randint(1,7)

    if randomNumber == 1:
        one +=1
    elif randomNumber == 2:
        two += 1
    elif randomNumber == 3:
        three += 1
    elif randomNumber == 4:
        four += 1
    elif randomNumber == 5:
        five += 1
    elif randomNumber == 6:
        six += 1

    cycle += 1
    
    if cycle == 1000:
        print('1: ' + str(one))
        print('2: ' + str(two))
        print('3: ' + str(three))
        print('4: ' + str(four))
        print('5: ' + str(five))
        print('6: ' + str(six))
        time.sleep(3)#input()
        cycle = 0
        letter = '$'