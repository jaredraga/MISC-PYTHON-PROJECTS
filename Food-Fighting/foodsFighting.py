#-*-coding:utf8;-*-
#qpy:3
#qpy:console

# Author: Jared I. Raga ©2018
# Email: jir@gmail.com
# Beginning  Date: ?/?/18
# Completion Date: ?/?/18
# Program Name: Foods Fighting (Testing Mechanic for an Upcoming Game of Mine)

#make currency from total Kills
#they would be able to buy items and weapons with sufficient kills

import random, time

print()

def displayHP():
    print('Egg\'s HP: ' + str(egg))
    print('Bacon\'s HP: ' + str(bacon))

def whoAttacksFirst():
    if random.randint(0, 1) == 0:
        return 'egg'
    
    else:
        return 'bacon'     

def playerAttacks(streak, kills):

    if kills > 1 and random.randint(1, 10) == 1:
        return kills * streak
    
    elif random.randint(1, 25) == 25: #4% chance that you would deal 0 damage 
        return 0           
           
    elif streak > 0:
        #if streak >= 5:
        #    return 5 
        #else:
        return streak * 2

    else: 
        return 1            

def isWinner(enemy):        
    if enemy < 1 and enemy == 0:
        return True

eggHP = 1000
baconHP = 1000

egg = eggHP
bacon = baconHP

eggStreak = 0
baconStreak = 0

eggKills = 0
eggDeaths = 0

baconKills = 0
baconDeaths = 0

someoneIsKilled = False

turn = whoAttacksFirst()
print('First Attack:' +turn)
print()

while True:
                      
    time.sleep(0.005)
        
    if turn == 'egg':
                
        damageToBacon = playerAttacks(eggStreak, eggKills)
        bacon = bacon - damageToBacon

        if damageToBacon > 0:
            eggStreak = eggStreak + 1
        else:
            eggStreak = 0
        
        displayHP()
        print()

        if bacon == 0 or bacon < 0:                
            print('bacon is killed!')
            #displayHP()
            #break
            eggKills = eggKills + 1
            baconDeaths = baconDeaths + 1
            someoneIsKilled = True                                
        
        else:
            turn = 'bacon'
    
    #time.sleep(1.5)
    
    else: # bacon's turn
        damageToEgg = playerAttacks(baconStreak, baconKills)
        egg = egg - damageToEgg

        if damageToEgg > 0:
            baconStreak = baconStreak + 1
        else:
            baconStreak = 0
       
        displayHP()
        print()

        if egg == 0 or egg < 0:                
            print('egg is killed!')
            #displayHP()                         
            #break
            baconKills = baconKills + 1
            eggDeaths = eggDeaths + 1
            someoneIsKilled = True
        
        else:
            turn = 'egg'

    if someoneIsKilled:
        egg = eggHP
        bacon = baconHP
         
        eggStreak = 0
        baconStreak = 0
        
        someoneIsKilled = False
        
        print()
        print('Bacon Kills:' + str(baconKills) + '   ' + 'Bacon Deaths:' + str(baconDeaths))
        print('Egg Kills:' + str(eggKills) + '   ' + 'Egg Deaths:' + str(eggDeaths))
       
        #time.sleep(5)
                                
        print()
        print('Rematching in...')
        print(3) 
        #time.sleep(1)
        print(2)
        #time.sleep(1)
        print(1)
        time.sleep(.1)
        
        turn = whoAttacksFirst()
        print('First Attack:' +turn)
        print()      

