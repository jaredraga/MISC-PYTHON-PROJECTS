import time

MAN = ['''
         π π    
         (O/
          |
         / \\''','''
         
        π  π    
         \O/
          |
         / \\''','''
     
       π
           π    
         \O/
          |
         / \\''','''          
  
     π
        
           π    
         \O/
          |
         / \\''','''
              
   π    
           π    
         \O/
          |
         / \\''','''
      
  π        π    
         \O/
          |
         / \\''','''
       
           π    
  π      \O/
          |
         / \\''','''
        
           π    
         \O/
  π       |
         / \\''','''
      
           π    
         \O/
          |
  π      / \\''','''
  
           π    
         \O/
          |
         / \\''']

SPACES = ['''


















































































                ''']

cycle = 0
while True:
    print(SPACES[0])    
    print(MAN[cycle])
    time.sleep(0.1)   
    cycle = cycle + 1    
    if cycle == 10:
        cycle = 0
