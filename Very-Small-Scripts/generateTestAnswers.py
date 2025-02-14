#Automatically Generate a random Answer Key for You


import random

dest = input('Save results to:')

dest = dest + '.txt'

def getListOfItems():
    print("Type 'done' to stop")
    print("Type 'restart' to restart choice") 
    print('The items to choose from:')
    items = []
    itemNumber = 1
    while True:
        choices = input('Item \#' + str(itemNumber) + ':')
        
        if choices.lower() == 'done':
            print('Done in choices')
            return items
        elif choices.lower() == 'restart':
            items = []
            itemNumber = 1
            print('Restarted, State choices again:') 
        else:
            items.append(choices)
            itemNumber += 1
        
def displayGenerated():
    with open(dest,'r') as f:
        data = f.readlines()
        for line in data:
            print(line)
        print('Results were written to: ' + dest)

def writeInFile(item, numbering):
    with open(dest,'a+') as f:
        f.writelines(str(numbering) + '. ')
        f.writelines(item)
        f.writelines('\n')       
        
def choosingItem(listOfItems):
    
    numbering = 0   
    while True:
        chosen = random.choice(listOfItems)
                       
        numbering += 1        
        writeInFile(chosen, numbering)
        
        if numbering >= int(howManyToProduce):
            break
            
    print('Finished generating ' + str(numbering) + ' items.')     

listOfItems = getListOfItems()
print(str(len(listOfItems)) + ' items')

howManyToProduce = input('How many items to produce:')
choosingItem(listOfItems)
displayGenerated()