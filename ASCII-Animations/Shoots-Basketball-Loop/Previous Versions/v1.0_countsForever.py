import time

SPACES = ['''














































             ''']

counts = 0

#Decrease code length
#Just multiply dashes and '×'s based on the count's number
def displayCounts1():
    print('                 ___')
    print('         Counts:[ ' +str(counts)+ ' ] ') 
    print('                ×××××')

def displayCounts10():
    print('                 ____')
    print('         Counts:[ ' +str(counts)+ ' ] ') 
    print('                ××××××')
                   
def displayCounts100():
    print('                 _____')
    print('         Counts:[ ' +str(counts)+ ' ] ') 
    print('                ×××××××')
def displayCounts1000():
    print('                 ______')
    print('         Counts:[ ' +str(counts)+ ' ] ') 
    print('                ××××××××')
def displayCounts10000():
    print('                 _______')
    print('         Counts:[ ' +str(counts)+ ' ] ') 
    print('                ×××××××××')
def displayCounts100000():
    print('                 ________')
    print('         Counts:[ ' +str(counts)+ ' ] ') 
    print('                ××××××××××')   
#million
def displayCounts1000000():
    print('                 _________')
    print('         Counts:[ ' +str(counts)+ ' ] ') 
    print('                ×××××××××××')
def displayCounts10000000():
    print('                 __________')
    print('         Counts:[ ' +str(counts)+ ' ] ') 
    print('                ××××××××××××')                                    
def displayCounts100000000():
    print('                 ___________')
    print('         Counts:[ ' +str(counts)+ ' ] ') 
    print('                ×××××××××××××')                                 
#billion
def displayCounts1000000000():
    print('                 ____________')
    print('         Counts:[ ' +str(counts)+ ' ] ') 
    print('                ××××××××××××××')
def displayCounts10000000000():
    print('                 _____________')
    print('         Counts:[ ' +str(counts)+ ' ] ') 
    print('                ×××××××××××××××')
def displayCounts100000000000():
    print('                 ______________')
    print('         Counts:[ ' +str(counts)+ ' ] ') 
    print('                ××××××××××××××××')
#trillion
def displayCounts1000000000000():
    print('                 _______________')
    print('         Counts:[ ' +str(counts)+ ' ] ') 
    print('                ×××××××××××××××××')                                       
def displayCounts10000000000000():
    print('                 ________________')
    print('         Counts:[ ' +str(counts)+ ' ] ') 
    print('                ××××××××××××××××××')                                       
def displayCounts100000000000000():
    print('                 _________________')
    print('         Counts:[ ' +str(counts)+ ' ] ') 
    print('                ×××××××××××××××××××')                                       
#quadrillion
def displayCounts1000000000000000():
    print('                 __________________')
    print('         Counts:[ ' +str(counts)+ ' ] ') 
    print('                ××××××××××××××××××××')                                       

while True:
    print(SPACES[0])
    if counts < 10 and counts > 0:
        displayCounts1()
    if counts < 100 and counts > 10:
        displayCounts10()
    if counts < 1000 and counts > 100:
        displayCounts100()
    if counts < 10000 and counts > 1000:
        displayCounts1000()
    if counts < 100000 and counts > 10000:
        displayCounts10000()
    if counts < 1000000 and counts > 100000:
        displayCounts100000()
    if counts < 10000000 and counts > 1000000:
        displayCounts1000000()
    if counts < 100000000 and counts > 10000000:
        displayCounts10000000()
    if counts < 1000000000 and counts > 100000000:
        displayCounts100000000()   
    if counts < 10000000000 and counts > 1000000000:
        displayCounts1000000000()   
    if counts < 100000000000 and counts > 10000000000:
        displayCounts10000000000()
    if counts < 1000000000000 and counts > 100000000000:
        displayCounts100000000000()   
    if counts < 10000000000000 and counts > 1000000000000:
        displayCounts1000000000000()   
    if counts < 100000000000000 and counts > 10000000000000:
        displayCounts10000000000000()   
    if counts < 1000000000000000 and counts > 100000000000000:
        displayCounts100000000000000()   


    time.sleep(1)        
           
    counts = counts + 1
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

points = 0
cycle = 0        
while counts >= 1000000000000000:
    
    print(SPACES[0])
    print(MAN[cycle])
    print('Points:' + str(points))            
    print('                 __________________')
    print('         Counts:[ 1000000000000000 ]') 
    print('                ××××××××××××××××××××')       
    print()
    print('You reached the end.')
    if points == 69:
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
                 __________________
         Counts:[ 1000000000000000 ]
                ××××××××××××××××××××
''']

GAMEOVER = '---GameOver---'

REACHED69 = 'You reached 69 points'

dash =  '-' * len(GAMEOVER)

dot = '•' * len(REACHED69)

while True:

    for i in range(len(GAMEOVER)):
        print(SPACES[0])
        print(ENDPIC[0])
        print(GAMEOVER[:i] + dot[i] + GAMEOVER[i+1:])
                
        time.sleep(0.2)
        
    for i in range(len(REACHED69)):
        print(SPACES[0])
        print(ENDPIC[0])
        print(REACHED69[:i] + dot[i] + REACHED69[i+1:])
                
        time.sleep(0.2)
    
    