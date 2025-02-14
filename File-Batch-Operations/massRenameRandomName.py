#7/14/18 3:50PM:
#By Me, ~Jared

import random, string, os

# select all files with the provided keywords
keyword = input('Files with keywords to rename(i.e:dog jpeg txt):')
keyword = keyword.split()

# counts the renamed files and directories
numberOfRenamedFiles = 0
numberOfRenamedDirs = 0

# this reiterates for every file or folder in the directory
for filename in os.listdir('.'):        
    
    # this runs for every keyword in the keyword list  	
    for mask in keyword:
        
        # if the keyword is in the name of the file/folder , that's only where it should start counting(cycle) the numbers , it should not count the directories/files that's not selected by us
        if mask in filename:            
            
            randomStr = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(8)) 

            # if the keyword it matches is a file
            if os.path.isfile(filename):   
                                                                                           
                # deletes the dot at the start of the filetype if there is one
                fileExt = filename[(len(filename)-4):].replace('.','')
                  
                newName = randomStr + '.' + fileExt
                
                # filename is the original name of our selected files , after the comma(,) is what it should be renamed to
                os.rename(filename, newName)

                print('Renamed ' + str(filename) + ' to ' + newName)                  
                numberOfRenamedFiles = numberOfRenamedFiles + 1
            
            # if the keyword it matches to rename is a directory/folder:
            else:
                          
                # we don't preserve the file extension because a directory doesn't have a file extension in the first place
                os.rename(filename, randomStr)
               
                print('Renamed directory ' + str(filename) + ' to ' + randomStr)
                numberOfRenamedDirs = numberOfRenamedDirs + 1
                
# if the keywords didn't match any files or folders
if numberOfRenamedFiles + numberOfRenamedDirs == 0:
    # these remove the strings '[', ']' and ''' in the list of keywords
    keyword = str(keyword).replace('[','')
    keyword = str(keyword).replace(']','')
    keyword = str(keyword).replace("'","")

    print('No file or directory have matched the keyword/s:' + '"' + str(keyword) + '"')
    
if numberOfRenamedFiles == 1:
    print('Finished renaming ' + str(numberOfRenamedFiles) + ' file')
elif numberOfRenamedFiles > 1:
    print('Finished renaming ' + str(numberOfRenamedFiles) + ' files')

if numberOfRenamedDirs == 1:
    print('Finished renaming ' + str(numberOfRenamedDirs) + ' directory')
elif numberOfRenamedDirs > 1:
    print('Finished renaming ' + str(numberOfRenamedDirs) + ' directories')
