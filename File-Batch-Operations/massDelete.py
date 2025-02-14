import os
import shutil

keywords = input('DELETE ALL files with keyword(e.g.:spam txt jpeg):')

confirm = input('Are you sure?(Deleting all directories with keywords \' ' + keywords + ' \'(y/n):')

keywords = keywords.split()

deletedDirs = 0
deletedFiles = 0

if confirm.lower().startswith('y'):

    for filename in os.listdir('.'):
    
        for item in keywords:
       
            if item in filename:
                                   
                if os.path.isdir(filename):   
                    print('Deleted directory: '+ filename)
                    shutil.rmtree(filename)
                    deletedDirs = deletedDirs + 1
                else:
                    print('Deleted file: '+filename)
                    os.remove(filename)
                    deletedFiles = deletedFiles + 1
                
else:
    print('Operation cancelled.')

if deletedFiles >= 1:
    print('Number of Deleted Files:' + str(deletedFiles))
if deletedDirs >= 1:
    print('Number of Deleted Folders:' + str(deletedDirs))
if deletedFiles and deletedDirs >= 1:
    print('Deleted Total:' + str(deletedFiles + deletedDirs))
if deletedFiles + deletedDirs == 0:
    print('No file/directory matched the given keyword/s')