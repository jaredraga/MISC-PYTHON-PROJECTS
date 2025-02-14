import time


MAN = ['''   
          π
          O
         /|\\
         / \\''','''    
                                 
          π
          O/
         /|
         / \\''','''  
         
          π\\
          O,
         /|
         / \\''','''         
         
           π
          O/
         /|
         / \\''','''            
            
          O
         /|\\π
         / \\''','''                           
         
           π
          O/
         /|
         / \\''','''        
         
          π\\
          O,
         /|
         / \\''','''
                
          π
          O/
         /|
         / \\''','''
         
          π
          O
         /|\\
         / \\''']
         
SPACES = ['''









































































































''']

#indexes to speed up:1 2 3 5 6 7
cycle = 0
while True:
    print(SPACES[0])    
    print(MAN[cycle])
    
    if cycle == 1 or cycle == 2 or cycle == 3 or cycle == 5 or cycle == 6 or cycle == 7:
        time.sleep(0.15)
    else:
        time.sleep(1.2)
     
    cycle = cycle + 1    
    if cycle == 9:
        cycle = 0
       
   
        
