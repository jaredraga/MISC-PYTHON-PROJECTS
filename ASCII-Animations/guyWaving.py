import time

MAN = ['''

 O
/|\\
/ \\''','''

 O/
/|
/ \\''','''

 O
/|\\
/ \\''']

 
SPACES = ['''











































































                ''']

cycle = 0
while True:
    print(SPACES[0])    
    print(MAN[cycle])
    time.sleep(0.8)   
    cycle = cycle + 1    
    if cycle == 3:
        cycle = 0
