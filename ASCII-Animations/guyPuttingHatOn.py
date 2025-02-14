#Guy putting hat on


import time

MAN = ['''

 O
/|\π
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

cycle = 0
while True:
    print(SPACES[0])    
    print(MAN[cycle])
    time.sleep(0.2)   
    cycle = cycle + 1    
    if cycle == 5:
        cycle = 0
