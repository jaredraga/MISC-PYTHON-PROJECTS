#Started
#6/23/18 5:00PM


#Lol wtf is happening here -5:20PM

import random, time

cycle = 0
progress = 0
loaded = 0

while True:#cycle <= 100:
    print('\n' * 30)
    #randomSleep = random.randint()

    #print('[' + ' ' * 34 + ']')
          
    print('[' + '=' * int(progress) + ' ' * (30 - int(progress)) + ']')
    print('Loaded ' +str(int(loaded))+ '%')
    print(str(cycle))
    
    #if cycle % 10 == 0:
    loaded = cycle + 1
    
    time.sleep(.01)
    
    if loaded % 3 == 0:
        progress = loaded/3
         
    #if progress == 1:
        #progress = 0
        
    if cycle == 100:
        cycle = 0
        input()
   
    cycle += 1