import time

MAN = ['''
   +
 O/
/|
/ \\''','''

 +
 O\\
/|
/ \\''']

 
SPACES = ['''











































































                ''']

cycle = 0
while True:
    print(SPACES[0])    
    print(MAN[cycle])
    time.sleep(0.7)   
    cycle = cycle + 1    
    if cycle == 2:
        cycle = 0
