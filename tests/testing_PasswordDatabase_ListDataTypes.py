#Testing List Data Types

#PASSWORD DATABASE
#Flow Chart:

#           Start
#   User types his password
#    Turn password to list
# Computer stores password in database
#           End


#user types their password
def typePassword(): 
    print('Enter your password:')
    password = input()
              
    return password

#computer stores password     
def storing(typedPassword):

    #if admin lists all password, computer wont store the command string    
    if password == 'listall':
        return passwordTable
        
    #adds password inside the database
    passwordTable.append(password)
    
    return passwordTable

    
passwordTable = ['keja133@-', '3-#+2888', 'password133', '@#-#-37', 'pass321']    

while True:

    password = typePassword()
    #lists all passwords    
    if password == 'listall':
        print(passwordTable)
        
        
    passwordTable = storing(password)
    
#success! -duck 4/21/18

    








 