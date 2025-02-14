import os

#6/1/18 9:50PM
#Yesss! I've been succesful!

# shortcut for calling os.system command
#t = os.system

toRename = input('Files to rename:') 
renameWith = input('Rename with:')

for i in range (1, 20):
    os.rename( toRename + str(i)+'.txt', renameWith +str(i)+'.txt')

print('Operation Success')
os.system('ls')