#Self-made HACKER TYPER©
#Creator is -Eend™
#On 5/1/18
#Within 10 to 20 Minutes

#Next time I want the message 
#being typed not shown to the 
#computer

import time, random

def hackerTyper():
    for i in range(len(text)):
    
        print(' ' * 2000)
    
        #text = text[:i] + text[i]
    
        print(text[:i + 1])#wtf, this works?
        #i dunno how or why..
            
        getDelay = random.randint(1, 2)
        if getDelay == 1:
            delay = 0.07
        else:
            delay = 0.09  
        time.sleep(delay)
        
        
while True:   
    text = input()
    hackerTyper()