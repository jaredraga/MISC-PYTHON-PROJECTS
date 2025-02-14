#def sayPassword(pword):
#    print('Password: ' + pword + ' ')

#print('Input your password')
#Jack = input()
#sayPassword(Jack)

#print('Input your password')
#Ryan = input()
#sayPassword(Ryan)

#success! -duck

def sayHello(name):
    print('Hello, ' + name + '')

import random

turns = 0

repeat = 'yes'
while repeat == 'yes' or repeat == 'y':
    while turns != 500:

        r = random.randint(1, 1000)
    
        sayHello(str(r))

        turns = turns + 1

        if r == 69:
            print()
            print('LOL, See that? 69')
            print()
            break
    