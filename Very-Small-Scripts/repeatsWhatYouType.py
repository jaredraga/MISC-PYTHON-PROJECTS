import random, time

print('Input what text:')
textUserWants = input()

print('Input how many times:')
loopsUserWants = int(input()) + 1

print('Input time interval(seconds):')
intervalUserWants = float(input())

#I did not include this code because this is not needed
#Asks for how many spaces inbetween each writes
#print('Input how many spaces after each writing:')
#numberOfSpaces = int(input()) - 1

loopsMade = 0
while True:
    #the range assigns how many loops should be made
    for item in range(1, +loopsUserWants):
        
        #print('\n' * numberOfSpaces)
                
        print()       
        print(textUserWants)
        
        #Every loops made:
        loopsMade = loopsMade + 1
        print('Times written: ' +str(loopsMade))    
        
        time.sleep(intervalUserWants)
    
    #stops the loop
    #continues with another hundred loops if User presses enter             
    input()   

#this works!
#i'll use this code block instead in the future
#this is efficient