import time
import random

RIGHT = ['''

→''','''

 →''','''
 
  →''']

LEFT = ['''

   ←''','''
    
  ←''','''
   
 ←''','''
  
←''']

SPACES = ['''















''']
def getRandom():
    arrow = random.randint(1, 2)
    
    return arrow
    
cycle = 0

while True:
    
    if cycle == 0:
        arrow = getRandom()
    
    while arrow == 1:
        print(SPACES[0])
        print(RIGHT[cycle])
        time.sleep(0.5)
        cycle = cycle + 1
        
        if cycle == 3:
            cycle = 0
            break
   
    while arrow == 2:
        print(SPACES[0])
        print(LEFT[cycle])
        time.sleep(0.5)
        cycle = cycle + 1
        
        if cycle == 4:
            cycle = 0
            break
        



#4/25/18 11:21AM
# still unsuccessful

#4/25/18 12:37AM
# success!