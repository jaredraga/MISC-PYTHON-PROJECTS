#-*-coding:utf8;-*-
#qpy:3
#qpy:console

# Author: Jared I. Raga ©2018
# Email: jir@gmail.com
# Beginning  Date: 6/1/18
# Completion Date: 6/1/18 9:15PM
# Program Name: String Reverser

import sys

#6/1/18 9:15PM:
#I've done it! Yesss

print('String Reverser')

while True:
    print()   
    string = input('String:')

    reversed = ''
    for i in range(len(string)):
        reversed += string[len(string) - (i + 1)]
        
    print('Reversed:' + reversed.lower())
    
    if string.lower() == reversed.lower():
        print('String is a palindrome.')

    