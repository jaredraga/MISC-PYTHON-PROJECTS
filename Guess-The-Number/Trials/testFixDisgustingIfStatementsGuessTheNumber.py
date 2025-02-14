#test

while True: 
    print('Guess goes here')
    guess = input()
    guessIsValid = False
    for i in range(len(guess)):
        if guess[i] in '0123456789':
            guessIsValid = True
            print('Valid!')              
        
        else:
            guessIsValid = False
            print('Please only enter NUMBERS!')
    
    if guessIsValid:
        guess = int(guess)
        
        if guess < 5:
            print('No guess less than 5!')
            
        elif guess > 50:
            print('No guess more than 50!')
                 
        else:
            break
   
        
print('Made it outside!')       
            
        
                    
               