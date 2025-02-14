import random
import time

SHOOTING = ['''
                                                                                      
    |                     
   (|\ /                   @ (
  =                        (O,
  =                         |
 ===                       / \\''','''
                                                                         
    |                     @
   (|\ /                     \\
  =                        \O,
  =                         |
 ===                       / \\''','''
                     
                       @
                         
    |                     
   (|\ /                     \\
  =                        \O,
  =                         |
 ===                       / \\''','''
 
                     @
                       
                         
    |                     
   (|\ /                     \\
  =                        \O,
  =                         |
 ===                       / \\''']      
     
      
SHOOT = ['''

                @ 
                  
                     
                       
    |                   
   (|\ /                     \\
  =                        \O,
  =                         |
 ===                       / \\''','''
                  
             @      
                     
                       
    |                   
   (|\ /                     \\
  =                        \O,
  =                         |
 ===                       / \\''','''
                                   
          @           
                       
    |                   
   (|\ /                     \\
  =                        \O,
  =                         |
 ===                       / \\''','''
                                                         
        @               
    |                   
   (|\ /                     \\
  =                        \O,
  =                         |
 ===                       / \\''','''
                                                                               
    |  @                 
   (|\ /                     \\
  =                        \O,
  =                         |
 ===                       / \\''','''
                                                                             
    |                    
   (|\@/                     \\
  =                        \O,
  =                         |
 ===                       / \\''','''
                                                                             
    |                    
   (|\ /                     \\
  =  @                     \O,
  =                         |
 ===                       / \\''','''
                                                                               
    |                   
   (|\ /                     \\
  =                        \O,
  =  @                      |
 ===                       / \\''','''
                                                                                
    |                    
   (|\ /                     \\
  =                        \O,
  =                         |
 === @                     / \\''','''       
                                                           
    |                  
   (|\ /                     \\
  =                        \O,
  =                         |
 ===                       / \\''']
       
MISS = ['''

                  @  
                     
                       
    |                    
   (|\ /                     \\
  =                        \O,
  =                         |
 ===                       / \\''','''
 
                    
               @      
                        
    |                    
   (|\ /                     \\
  =                        \O,
  =                         |
 ===                       / \\''','''
 
                    
                     
             @           
    |                   
   (|\ /                     \\
  =                        \O,
  =                         |
 ===                       / \\''','''
 
                   
                     
                        
    |      @              
   (|\ /                     \\
  =                        \O,
  =                         |
 ===                       / \\''','''
 
                    
                      
                        
    |                    
   (|\ / @                   \\
  =                        \O,
  =                         |
 ===                       / \\''','''
 
                    
                      
                        
    |                    
   (|\ /                     \\
  =     @                  \O,
  =                         |
 ===                       / \\''','''

                   
                     
                        
    |                    
   (|\ /                     \\
  =                        \O,
  =    @                    |
 ===                       / \\''','''
 
                    
                      
                        
    |                    
   (|\ /                     \\
  =                        \O,
  =                         |
 ===  @                    / \\''','''
                         
    |                    
   (|\ /                     \\
  =                        \O,
  =                         |
 ===                       / \\''']
        
#         @
#    |  @   @
#   (|\@/----@--   	
#  =   @      \O/
#  =   @       |
# ===  @      / \\''','''



#                 @ 
#             @    @  @
#          @    @       @
#        @    @           @
#    |  @   @              @
#   (|\@/ @                 @ \\
#  =   @ @                  \O,
#  =   @@                    |
# ===  @                    / \\
  
SPACES = ['''


















































































                ''']












#SHOOTINGcycle = 0
#MISScycle = 0
#SHOOTcycle = 0
#shoot = 1
#miss = 2
#shooting = random.randint(1, 2)
#while True:
#    
#    if shooting == shoot:
#        print(SPACES[0] + SHOOTING[SHOOTINGcycle] + SPACES[0] + SHOOT[SHOOTcycle])
#    if shooting == miss:
#        print(SPACES[0] + SHOOTING[SHOOTINGcycle] + SPACES[0] +MISS[MISScycle])        
#    
#    time.sleep(0.1)
#    
#    SHOOTINGcycle = SHOOTINGcycle + 1
#    if SHOOTINGcycle == 4:
#        SHOOTINGcycle = 0
#        
#    MISScycle = MISScycle + 1
#    if MISScycle == 9:
#        MISScycle = 0
#        
#    SHOOTcycle = SHOOTcycle + 1
#    if SHOOTcycle == 10:
#        SHOOTcycle = 0

# success! -duck
# 4/25/18 1:14PM

def getRandom():
    event = random.randint(1, 2)  
    
    return event
      
cycle = 0
shoots = 0
misses = 0

#Constant variables
SHOOTEVENT = 1
MISSEVENT = 2

while True:

    if cycle == 0:
        event = getRandom()    
    	    
    while event == SHOOTEVENT: 
        while cycle < 4:
            print(SPACES[0])
            print(SHOOTING[cycle])
                
            #print('Shoots:' + str(shoots))
            #print('Misses:' + str(misses))   

            time.sleep(0.06)
        
            cycle = cycle + 1
        
        cycle = 0 
          
        while cycle < 10:
            print(SPACES[0])
            print(SHOOT[cycle])
           
            if cycle == 8:
                shoots = shoots + 1
            #print('Shoots:' + str(shoots))
            #print('Misses:' + str(misses))
            
            time.sleep(0.06)
            

            cycle = cycle + 1
            
        if cycle == 10:
            cycle = 0
            break
    
    while event == MISSEVENT:
        while cycle < 4:
            print(SPACES[0])
            print(SHOOTING[cycle])
            
            #print('Shoots:' + str(shoots))
            #print('Misses:' + str(misses))   
            
            time.sleep(0.07)
        
            cycle = cycle + 1
        
        cycle = 0
             
        while cycle < 9:
            print(SPACES[0])
            print(MISS[cycle])
            
            if cycle == 7:
                misses = misses + 1
            #print('Shoots:' + str(shoots))
            #print('Misses:' + str(misses))   
          
            time.sleep(0.07)
               
            cycle = cycle + 1
    
        if cycle == 9:
            cycle = 0
            break
    
                      
