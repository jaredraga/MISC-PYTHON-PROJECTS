#created a function 'testTest()'
def testTest():
    #prints the string variable 'name' from the global scope
    print('' + name + ' ')
    #prints the integer variable 'testGuessesTaken' and adds 999999999 to its value 
    print(testGuessesTaken + 999999999)
    #return keyword makes the computer exit the def block
    return

#creates a variable 'test' with a string value of 1
test = '1'

#creates variable 'testGuessesTaken' with an integer value of 1
testGuessesTaken = 1

#makes a while loop with condition that - while 'test' variable is equal to the string value of '1', the loop continues to play
while test == '1':
    
    #prints string 'Test, give name'
    print('Test, give name')
    #records the input of the user to variable 'name'
    name = input()

    #calls the created function 'testTest()'
    testTest()

    #prints string '1/2?'
    print('1/2?')
    #records the input of the user to variable 'test'
    test = input()

#success! -duck