#Tao o Ibon
#2-digit dice
#4/23/18

import random

PISO = ['''

 -------
-T      -
-   A   -
-      O-
 ------- ''','''

 -------
-       -
-I B O N-
-       -
 ------- ''']
 
 

while True:    
    pickSide = random.randint(1, 2)
    print(PISO[pickSide - 1])
    
    input()

    