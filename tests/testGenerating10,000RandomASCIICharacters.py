#Created by -Anatra 
# April 28, 2018

import random, string, time

ASCII = 'a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 1 2 3 4 5 6 7 8 9 0 @ $ % & - + ( ) * " : ; ! ? , _ / ~ ` | √ π ÷ ^ = { } \\ [ ] < > \' '.split()

cycle = 0

print('How many characters to generate:', end = '')
limit = input()

while True:
    cycle = cycle + 1

    choosingRandom = random.randint(0, len(ASCII))

    print(ASCII[choosingRandom - 1])

    time.sleep(0.01)    

    if cycle == int(limit):
        break

print()
print('Generated Characters: ' + limit + ' ')