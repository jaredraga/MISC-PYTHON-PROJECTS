with open('testAccounts.txt') as filehandle: 
    lines = filehandle.readlines() 

with open('testAccounts.txt', 'w') as filehandle: 
    lines = filter(lambda x: x.strip(), lines) 
    filehandle.writelines(lines) 