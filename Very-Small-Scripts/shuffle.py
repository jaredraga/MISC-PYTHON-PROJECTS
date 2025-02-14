#Beginning: 7/26/18 11:25
#Completion: 7/26/18 

# Rearranges the given string()

import random

def generate(word, times):
    generated = [word]
    print(word)
    times_shuffled = 0
    while True:          
        list_word = list(word)
        random.shuffle(list_word)
        shuffled = ''

        for i in range(len(list_word)):
            shuffled += list_word[i]
        
        if shuffled == word or shuffled in generated:
            continue

        print(shuffled)
        times_shuffled += 1
        generated.append(shuffled)
        if times_shuffled >= times:
            print()
            break

print('Press CTRL-C to quit.')
print('Usage:<your word> <times to shuffle>')
print()
try:
    while True:
        inp = input('Type here:')
        inp = inp.split()
        the_word = inp[0]
        times = int(inp[1])

        generate(the_word, times)
except KeyboardInterrupt:
    print('\nExited.')

