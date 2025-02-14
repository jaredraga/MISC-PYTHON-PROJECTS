def displayHallOfFame():
       
    with open("gtLogTest.txt","r") as f: 
        data = f.readlines()        
        sortedData = sorted(data, key=lambda item: int(item.split()[1]), reverse=True)
        top = sortedData[:10]
        number = 1
        print('~ ~ ~ HALL OF FAME ~ ~ ~')
        for user in top:
            stats = user.split()
            print(str(number) + '.' + ' ' * (2 - len(str(number))) + stats[0] + ' ' * ((13 - len(stats[0]))) + stats[1])
            number += 1

displayHallOfFame()