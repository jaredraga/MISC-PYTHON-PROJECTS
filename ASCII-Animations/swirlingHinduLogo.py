#Logo Swirling

import time

LOGO = ['''

↑    →→→
↑    ↑
↑←←®→→↓
    ↓  • ↓
←←←    ↓''','''


↑    →→→
↑    ↑
↑←←®→→↓
  • ↓    ↓
←←←    ↓''','''


↑    →→→
↑ •  ↑
↑←←®→→↓
    ↓    ↓
←←←    ↓''','''


↑    →→→
↑    ↑ •
↑←←®→→↓
    ↓    ↓
←←←    ↓''']



cycle = 0
while True:  
    print(' ' * 1000)  
    print(LOGO[cycle])
        
    cycle = cycle + 1    
    if cycle == 4:
        cycle = 0
    
    time.sleep(0.1)




    