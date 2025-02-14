def displayStats(currentUsername):
    with open("gtLogTest.txt","r") as f: 
        data = f.readlines()             
        for line in data:
            userData = line.split()                             
            if str(currentUsername) == str(userData[0]):
                print('User: ' + userData[0] + ' ' * ((11 - len(userData[0]))) + 'Highscore:' + userData[1])

displayStats('Scalifra')