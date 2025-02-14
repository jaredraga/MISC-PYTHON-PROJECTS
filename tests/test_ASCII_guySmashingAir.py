import time

MAN = ['''
  
  @
  O)
 /|
@/ \\ ''','''

    -, 
    @–' 
  O/ '
 /|
@/ \\''','''
 
       ,
  -       '
        
    @    
  O/       –
 /|      '
@/ \\''']

#give smash effects
#


 
SPACES = ['''











































































                ''']

cycle = 0
while True:
    print(SPACES[0])    
    print(MAN[cycle])
    time.sleep(0.1)   
    cycle = cycle + 1    
    if cycle == 3:
        cycle = 0

#Doesn't really look like a guy smashing the air