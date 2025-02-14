
def fileNumbering():
    print('Input starting number')
    startingNumber = input()
    print('Input ending number')
    endingNumber = input()
    print()
    
    #multiplies the zeros depending on the max number
    zeros = '0' * len(endingNumber)

    #prints the number sequence
    # the '+1' in the for loop is because the range always counts 1 below the assigned max number
    for i in range(int(startingNumber), int(endingNumber)+1):
        
        i = str(i)
        #the zeros added in front depends on the max number 
        #'zeros[0:len(zeros)-len(i)]'
        #    'zeros[]' slices the string value of zero into multiple parts
        #        example: if the zeros variable = '12345'
        #        ,and slice zeros like 'zero[1:4]', then you would get the numbers:'234'
        #        because you sliced the string between index[1](the string '2') and index[4](the string '5')
        #        //note:indexes starts at '0' so when you call the index '0' you would get the string '1'
        #    '[0:len(zeros)-len(i)]' counts the character count of zeros -(minus) the character count of i(which is our number)
        print(zeros[0:len(zeros)-len(i)] + i) 

programIsDone = False
while programIsDone == False:
    fileNumbering()
    print('Again [Y/n]')
    if input().lower().startswith('y'):
        programIsDone = False
    else:
        programIsDone = True