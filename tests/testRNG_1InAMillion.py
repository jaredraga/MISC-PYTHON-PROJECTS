import random, time

    
cycle = 0
takeAgain = ''
while takeAgain == '':
    if cycle == 0:
        print('Rolls to take:')
        rollsToTake = input()
    rareThing = 1 #random.randint(1, 1000000)

    chance = random.randint(1, 1000000)

    if chance == rareThing:
        print('Ultra-rare thing happened')
        print('Rolls:' + str(cycle + 1))
        break

    print(' ' * 100)
    print(chance)
    print('Rolls:' + str(cycle + 1))
    time.sleep(0.01)
    cycle = cycle + 1
    
    if cycle == int(rollsToTake):
        print(' ' * 100)
        print('Rolls Made:' + str(cycle))
        print('Take bet again?')
        takeAgain = input()  
        if takeAgain == '':
            cycle = 0        