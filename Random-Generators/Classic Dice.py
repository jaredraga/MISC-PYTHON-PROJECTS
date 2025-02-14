#Dice
# Created by -Duck™
#4/23/18

# Author: Jared I. Raga ©2018
# Email: jir@gmail.com
# Beginning  Date: 4/23/18
# Completion Date: 4/23/18
# Program Name: Lucky Dice

import random
from time import sleep
DICE = ['''
-------
-     -
-  •  -|1
-     -
-------''','''
-------
-    •-
-     -|2
-•    -
-------''','''
-------
-    •-
-  •  -|3
-•    -
-------''','''
-------
-•   •-
-     -|4
-•   •-
-------''','''
-------
-•   •-
-  •  -|5
-•   •-
-------''','''
-------
-•   •-
-•   •-|6
-•   •-
-------''']

#print('Press \'enter\' to roll the dice.')

while True:
   
    #print()
    #print('---------')
    
    #dicesToRoll = input()
   
    diceNum = random.randint(1, 6)
    
    print(DICE[diceNum - 1])
      
    #sleep(0.08)
    input()
    
