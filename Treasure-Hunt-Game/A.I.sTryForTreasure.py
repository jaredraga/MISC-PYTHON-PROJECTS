#-*-coding:utf8;-*-
#qpy:3
#qpy:console

# Author: Jared I. Raga ©2018
# Email: jir@gmail.com
# Beginning  Date: 5/31/18
# Completion Date: 5/31/18
# Program Name: A.I. Try For Treasure

#5/31/18

import random, time

print("This is console module")

alexTries = 0
alexRiceBuns = 0
alexTreasures = 0


linFanTries = 0
linFanRiceBuns = 0
linFanTreasures = 0

def alexTrying(totalTries, totalRiceBuns, totalTreasures):
    currentTries = 0
    while currentTries < 10000:     
        trying = random.randint(1, 10000)
        
        if trying == treasure:
            totalTreasures = totalTreasures + 1
        else:
            totalRiceBuns = totalRiceBuns + 1    
        currentTries = currentTries + 1
        totalTries = totalTries + 1   

    return totalTries, totalRiceBuns, totalTreasures
def linFanTrying(totalTries, totalRiceBuns, totalTreasures):
    currentTries = 0
    while currentTries < 10000:     
        trying = random.randint(1, 10000)
        
        if trying == treasure:
            totalTreasures = totalTreasures + 1
        else:
            totalRiceBuns = totalRiceBuns + 1    
        currentTries = currentTries + 1
        totalTries = totalTries + 1  

    return totalTries, totalRiceBuns, totalTreasures

cycle = 1
while True:
    
    treasure = random.randint(1, 10000)

    alexTries, alexRiceBuns, alexTreasures = alexTrying(alexTries, alexRiceBuns, alexTreasures)
    linFanTries, linFanRiceBuns, linFanTreasures = linFanTrying(linFanTries, linFanRiceBuns, linFanTreasures)
        
    leftSpaces = ' ' * (14 - len(str(alexTreasures) + str(alexTries)))
    rightSpaces = ' ' * (9 - len(str(linFanTreasures)))
    
    if cycle == 20:   
        print('Alex:' + str(alexTreasures) + leftSpaces + str(alexTries) + rightSpaces + str(linFanTreasures) + ':Lin Fan')
        cycle = 0
            
    else:
        print('    :' + str(alexTreasures) + leftSpaces + str(alexTries) + rightSpaces + str(linFanTreasures) + ':       ')
        
    
    cycle = cycle + 1
    
    time.sleep(0.0001)
