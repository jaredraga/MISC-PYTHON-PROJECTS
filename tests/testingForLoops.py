import random, time

abc = ['a', 'b', 'c']
while True:
    #the range assigns how many loops should be made
    for item in range(1, 100):
        #chooses random letter from abc and prints it        
        x = random.randint(0, 2)
        print(abc[x])     
        time.sleep(0.04)
    
    #stops the loop
    #continues with another hundred loops if I responded                
    input()   

#this works!
#i'll use this code block instead in the future
#this is efficient