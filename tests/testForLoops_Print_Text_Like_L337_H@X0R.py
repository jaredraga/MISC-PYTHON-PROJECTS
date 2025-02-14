#Self-made HACKER TYPER©
#Creator is -Eend™
#On 5/1/18
#Within 10 to 20 Minutes

#Next time I want the message 
#being typed not shown to the 
#computer

import time

def hackerTyper():
    for i in range(len(text)):
    
        print(' ' * 1000)
    
        #text = text[:i] + text[i]
    
        print(text[:i + 1])#wtf, this works?
        #i dunno how it does
            
        time.sleep(0.07)

while True:   
    text = input()
    hackerTyper()