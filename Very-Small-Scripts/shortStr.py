# 7/19/18 3:40PM
# By Jared Raga

# This script is really simple
# It produces a short, alphabetical string

# Uses:
# Shortening website links
# Generating random filenames

import random
import time
import string as s

def writeStr(shortStr):
    
    with open('shortStr.txt','a+') as f:
        f.writelines(shortStr)
        f.writelines('\n')              
        
# It's easier to import the letters
lettersList = list(s.ascii_uppercase + s.ascii_lowercase)

shortStr = ''

while True:

    for i in range(40):    
        
        for i in range(7):        
            shortStr += random.choice(lettersList)                           
        shortStr = shortStr + ' '
        
        if len(shortStr.split()) >= 4:
            print(shortStr)
            
            writeStr(shortStr)
            
            shortStr = ''
                
    time.sleep(0.1) 
    