# Author: Jared I. Raga ©2018
# Email: jir@gmail.com
# Beginning  Date: 5/12/18
# Completion Date: 5/12/18 8:40PM
# Program Name: Big Number Mania


#5/12/18 8:40PM
#This script tells you what that Big Number 
#with THAT many Zeros is really called
#It's just a variation of the other one, really
#but this is easier to use :) 

#I got the Big Number Names List here:
#http://lcn2.github.io/mersenne-english-name/tenpower/tenpower.html

with open('big_number_names.txt','r') as f:
	BIG_NUMBER_NAMES = f.read()

maxNumber = len(BIGNUMBERNAMES) - 1

def countZeros():
    
    while True:
        print('# of Zeros:', end = ' ')   
        zerosCount = input()
        
        if int(zerosCount) >= maxNumber + 1:
            print('------ ------ ------ ------ ------')
            print('Sorry, maximum number I currently')
            print('have is ' + BIGNUMBERNAMES[maxNumber])
            print('or 10^' + str(maxNumber) + '(1 with ' + str(maxNumber) + ' zeros)')
            print('------ ------ ------ ------ ------')
        elif zerosCount == '100':
            print('Googol Number! \n...(or ' + BIGNUMBERNAMES[100] + ')')
        else:
            print(BIGNUMBERNAMES[int(zerosCount)])
        print()
        print()

print()     
print('''

------ ------ ------ ------ ------
Welcome, 
------ ------ ------ ------ ------
Just put in how many 

zeros are in your number
------ ------ ------ ------ ------
I\'ll find out what that 

BIG NUMBER is called for you.   
------ ------ ------ ------ ------
	
        ''')
	
countZeros()
