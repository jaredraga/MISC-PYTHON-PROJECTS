#-*-coding:utf8;-*-
#qpy:3
#qpy:console

# Author: Jared I. Raga ©2018
# Email: jir@gmail.com
# Beginning  Date: 6/1/18
# Completion Date: 6/1/18 9:25PM
# Program Name: Vowel Counter

#6/1/18 9:25PM:
#Yess I've made it!

print('I count vowels')

totalVowels = 0
currentVowels = 0

while True:    
    word = input('>')
    
    for letter in word:
        if letter in 'a e i o u'.split():
            currentVowels = currentVowels + 1
            totalVowels = totalVowels + 1
    
    print(str(currentVowels) + ' vowel(s) in word')
    print('Total vowels: ' + str(totalVowels))
    print()
    currentVowels = 0
       
