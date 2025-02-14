import random

number = ' '

while True:

    input()
    
    for i in range(0,4):
        r = random.randint(1, 9)

        number += str(r)


    print(number)
    number = ''
