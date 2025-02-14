import time

counts = 0

#Decrease code length
#Just multiply dashes and '×'s based on the count's number
def displayCounts():
    dash = '_' * len(str(counts))
    cross = '×' * len(str(counts))
    spaces = ' ' * len(str(counts))
    
    #print('                 __'+dash)
    #print('         Counts:[ ' +str(counts)+ ' ] ') 
    #print('                ××××'+cross)

    print('                [ '+spaces+' ] ')
    print('         Counts:{ ' +str(counts)+ ' } ') 
    print('                [ '+spaces+' ] ')

#       [      ]      
#Counts:{ 1001 }
#       [      ]     
       
       	
while True:
    print(' ' * 3000)#spaces
    displayCounts()  

    time.sleep(1)#1 count per second      
           
    counts = counts + 100000000000000
    
    #1 quadrillion/31 million years
    if counts >= 1000000000000000:
        break

MAN = ['''

         
    |    
   (|\ /     @
  =          (O/
  =           |
 ===         / \\''','''
         
         
    |     
   (|\ /    @   	
  =          \O/
  =           |
 ===         / \\''','''
     
         
    |      @
   (|\ /       	
  =          \O/
  =           |
 ===         / \\''','''
   
         @
    |      
   (|\ /       	
  =          \O/
  =           |
 ===         / \\''','''
              
         
    |  @   
   (|\ /       	
  =          \O/
  =           |
 ===         / \\''','''
      
           
    |     
   (|\@/       	
  =          \O/
  =           |
 ===         / \\''','''
       
                               
    |     
   (|\ /      	
  =   @      \O/
  =           |
 ===         / \\''','''
        
               
         
    |     
   (|\ /       	
  =          \O/
  =   @       |
 ===         / \\''','''
      
               
         
    |     
   (|\ /       	
  =          \O/
  =           |
 ===  @      / \\''','''
  
               
                  
    |      
   (|\ /      	
  =          \O/
  =           |
 ===         / \\''']

points = 69
cycle = 0        
while counts >= 1000000000000000:
    
    print(' ' * 3000)
    print(MAN[cycle])
    print('Points:' + str(points))            
    print('                [                  ]')
    print('         Counts:{ 1000000000000000 }') 
    print('                [                  ]')       
    print()
    print('You reached the end.')
    if points >= 69:
        break
    
        
    time.sleep(0.3) 
    
    if cycle == 6:
        points = points + 1            
    cycle = cycle + 1
    if cycle == 10:
        cycle = 0
        

ENDPIC = ['''

    |     
   (|\ /       	
  =          \O/
  =   @       |
 ===         / \\
Points:69
                [                  ]
         Counts:{ 1000000000000000 }
                [                  ]
''']

GAMEOVER = '---GameOver---'

REACHED69 = 'You reached 69 points'

dash =  '-' * len(GAMEOVER)

dot = '•' * len(REACHED69)

while True:
    for i in range(len(REACHED69)):
        print(' ' * 3000)
        print(ENDPIC[0])
        print(REACHED69[:i] + dot[i] + REACHED69[i+1:])
                
        time.sleep(0.2)
    
    
    for i in range(len(GAMEOVER)):
        print(' ' * 3000)
        print(ENDPIC[0])
        print(GAMEOVER[:i] + dot[i] + GAMEOVER[i+1:])
                
        time.sleep(0.2)
        
    