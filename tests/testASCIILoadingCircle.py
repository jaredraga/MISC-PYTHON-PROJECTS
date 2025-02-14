#Logo Swirling

import time

LOGO = ['''
 \\
   o  
      ''','''
 
   | 
   o  
      ''','''
      
     /
   o  
      ''','''
      
    
   o -
      ''','''
      
    
   o  
     \\''','''

   o  
   |  ''','''
   
    
   o  
 /    ''',''' 

 - o  
      '''] 	         


cycle = 0
while True:  
    print(' ' * 1000)  
    print(LOGO[cycle])
        
    cycle = cycle + 1    
    if cycle == len(LOGO):
        cycle = 0
    
    time.sleep(0.5)
