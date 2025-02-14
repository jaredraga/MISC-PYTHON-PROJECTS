# Author: Jared I. Raga ©2018
# Email: jir@gmail.com
# Beginning  Date: 5/12/18
# Completion Date: 5/12/18
# Program Name: Character Counter


print('How many characters?')

print(''' 

-----  ------  ------ ------

This code just tells you how 

many characters there are in 

your input.

(what you typed/pasted)

-----  ------  ------ ------

      ''')

while True:
    print('Input:', end = '')
    userInput = input()

    characterCount = len(userInput)

    print()
    print('Character count = ' + str(characterCount) + ' ')
    print()