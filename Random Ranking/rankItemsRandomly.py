#Started on
#6/27/18

import random

einstein = ['Icka','Matthew','Vinsey','King Arvie','Denise','Lizel','Keith','Kate','Ella','Zandy','Charm','Casey','Cassey','Nataleigh','Kean','Aspen','Peter Lloyd','Markevin','Kendrick','IC','Markjay','Cedric','Xeven','John Carl','Paul','Cerra','Elmira']
buys = ['SSD','Phone','Keyboard']

listOfItems = buys #einstein

dest = 'itemRanking.txt'

def writeInFile(item, numbering):
    with open(dest,'a+') as f:
        f.writelines(str(numbering) + '. ')
        f.writelines(item)
        f.writelines('\n')
        
def isRepeated(person, ranked):
    for item in ranked:
        if item == person:
            return True
    
    return False
        
def choosingItem(listOfItems):
    
    numbering = 0
    alreadyRanked = []
    while True:
        chosen = random.choice(listOfItems)
               
        if not isRepeated(chosen, alreadyRanked):
            numbering += 1
            alreadyRanked.append(chosen)
            writeInFile(chosen, numbering)
        
        if numbering >= len(listOfItems):
            break
            
    print('Finished ranking ' + str(numbering) + ' items.')  

print(len(listOfItems))
choosingItem(listOfItems)