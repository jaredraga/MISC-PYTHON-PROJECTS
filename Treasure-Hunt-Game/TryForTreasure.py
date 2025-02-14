#-*-coding:utf8;-*-
#qpy:3
#qpy:console

# Author: Jared I. Raga ©2018
# Email: jir@gmail.com
# Beginning  Date: ?/?/18
# Completion Date: ?/?/18
# Program Name: Treasure Trying

import random, time

print("This is console module")

treasure = random.randint(1, 10000)

tries = 0

goodCurse = ['Ho ho ho a fucking ', 'That\'s what I\'m talking about! A ', 'Hell to the motherfucking yeah, a ', 'Ohhhh shit a motherfuckiiiing ', 'Fuck yeah a fucking ']

#badCurse = ['What the fuck a ', 'Bastard, it\'s a fucking ', 'Fuck me, it\'s a goddamned ', 'Are you fucking kidding me, A ', 'Fuck I\'m so fucking lucky, it\'s a ']

totalRiceBuns = 0
totalTreasures = 0

while True:
    #shoots for number randomly for a chance to get a treasure
    trying = random.randint(1, 10000)
        
    if trying == treasure:
        #adds treasure to total treasure and subtracts one to total rice bun
        totalRiceBuns = totalRiceBuns - 1
        totalTreasures = totalTreasures + 1    
       
        print('Total Rice Buns:' + str(totalRiceBuns))
        print('Treasures:' + str(totalTreasures))
 
     
        # chooses a random curse to say everytime you win
        randomCuss = random.randint(0, len(goodCurse) - 1)        
        print(goodCurse[randomCuss] + 'Treasure!')

        #resets the treasure's position everytime you win
        treasure = random.randint(1, 10000)
        
        print(str(tries) + ' tries')       
                       
        #resets tries to 0 after you win
        tries = 0
        
        print()
        #time.sleep(3)
        input('Press enter to test your luck again')
        
        
    else:
        # tells you everytime you get a rice bun
        print('Rice bun(' + str(tries) + ')')

    #counts the tries taken           
    tries = tries + 1
    
    totalRiceBuns = totalRiceBuns + 1        
    