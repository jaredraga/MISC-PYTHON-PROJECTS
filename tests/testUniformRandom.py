import random
import time 
import sys 

print('Loading User Data:')
r = random.randint(62, 84)

while True:
    for i in range(21):
        
        randomLetters = '@ 3 1 9 ) - & 6 * ; • ¥ ± < > !'.split()
        
        randomChar = random.choice(randomLetters)
        
        bar = randomChar * i
        loadingBar = '['+ bar + ' ' * (20 - len(bar)) +']'
        if i > r:
            t = random.uniform(0.1,0.02)
        else:
            t = random.uniform(.01, .02)
        time.sleep(t)     
        sys.stdout.write("\r%s" % loadingBar) 
        sys.stdout.flush()
    
    print('\nLoading complete')
        
    