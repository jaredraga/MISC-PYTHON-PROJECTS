from random import randint

print("'Random Number Chooser'")

while True:
    print()
    print()    
    startingNumber = input('Enter your starting number: \n>')    

    print()
    endingNumber = input('Your ending number: \n>')
  
    
    chooseRandom = randint(int(startingNumber), int(endingNumber))
    
    print()
    print('Chosen number is:' +str(chooseRandom))