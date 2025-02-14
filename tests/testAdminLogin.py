# 6/15/18 7:00AM

from getpass import getpass
from time import sleep

def login():
    print('-' * 34)
    username = input('User: ') 
    password = getpass('Pass: ')
    sleep(1)
    print('Processing...')
    sleep(3)
    for line in open('testAdminAcc.txt','r').readlines(): # Read the lines 
        login_info = line.split() # Split on the space, and store the results in a list of two strings 
        if username == login_info[0] and password == login_info[1]:
            print()
            print('Welcome to the CDDIS\' main database') 
            
            return True       
    print('Incorrect credentials!') 
    return False

sleep(2)
print(' CASPER DISRICT\'S DATACENTRE INFORMATIVE SYSTEM ')
sleep(3)

print()
print('You need to log-in to be authorized the information inside the database.')

tries = 0
while tries <= 3:
    sleep(2)
    print()
    print('LOGIN ' + ' ' * 24 + ' ' +str(tries)+'/3')
    if login():
        sleep(3)
        print()
        print('Modules:')
        print('''1.Genome Sequencing
2.CRISPR
3.Genetic Transformation
4.Unknown Transmutations
5.Level 5 Classified
6.Level 6 Classified
7.Level 7 Classified
8.Level 8 Classified
9.Level 9 Classified''')
        while True:
            moduleChoice = input()
           
            if len(moduleChoice) > 1:
                print('Error')
                print()
            elif moduleChoice not in '1234567890':
                print('Error')
                print()
            elif str(moduleChoice) in '56789':
                print('You are not authorized to access Level ' + str(moduleChoice) + ' information!')
                print()
            else:
                print('Please wait...')
                print()
    else:
        tries = tries + 1