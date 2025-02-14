#Dice
# Created by -Duck™
#4/23/18

import random

DICE = ['''

-------
-     -
-  •  -|1
-     -
-------''','''

-------
-•    -
-     -|2
-    •-
-------''','''

-------
-     -
-• • •-|3
-     -
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
#input()

while True:
    diceNum = random.randint(0, 5)
    
    print(DICE[diceNum])
    input()   
