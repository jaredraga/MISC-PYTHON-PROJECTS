#Beginning: 7/26/18 11:25
#Completion: 7/26/18 

# Rearranges the given string()

import random

the_word = 'cat'

def generate(word):
    while True:          
        word = list(word)
        random.shuffle(word)

        shuffled = ''
        for i in range(len(word)):
            shuffled += word[i]
        print(shuffled)
        word = input()


