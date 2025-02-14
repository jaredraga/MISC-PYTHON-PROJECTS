#6/1/18 9:05PM:
#By Me, ~Duck
#11:46PM
#Success!!! I've successfully configured the correct amount of zeros!

#Wow, I've tested the code. It's a beauty...
#It's now ready to get released into the wild...

#Update: 6/10/18 2:05PM:
#Added the renaming distinction between a file and a directory at line 60

#Bug: 6/10/18 2:35PM:
#It doesn't add a zero in front of '9' when numbering
#It only happens in '9' and nothing else

#6/12/18 9:15AM
#Adding the smart prompt. Knows if there are only files or only directories

import os, os.path

# select all files with the provided keywords
keyword = input('Files with keywords to rename(e.g:dog jpeg txt):')
keyword = keyword.split()

# rename all selected files with the same title
renameWith = input('Rename with title:')

# format of files being renamed 
# $EXPIRED: replaced with fileExt = filename[(len(filename)-4):].replace('.','')
# renameWithExt = input('Files to rename format (e.g.: \'txt,jpg,mp3\'):') 

# set file numbering to start at arranged value
fileNumber = input('Begin renaming files at number:')
fileNumber = int(fileNumber) - 1

# set directory numbering to start at arranged value
dirNumber = input('Begin renaming dirs at number:')
dirNumber = int(dirNumber) - 1


# counts the renamed files
renamed = 0

for filename in os.listdir('.'):        
        	
    for mask in keyword:
        # if the keyword is in the filename , that's only where it should start counting(cycle) the numbers , it should not count the directories/files that's not selected by us
        if mask in filename:            
            renamed = renamed + 1

               
                # adds one to the the file number everytime we rename a single file
                fileNumber = fileNumber + 1

                
                # configures how many zeros to put depending on the total number of files
                # len(os.listdir('.') counts how many files there are. in the directory
                # len(str(os.listdir('.'))) counts the characters of the number of files 100 == 3 characters, 20 == 2 characters
                # len(str(cycle + 1)) subtracts the zeros based on the character count of the file number , if 100 is the max there should be NO zero in front of 100(0100), but there should be a zero in front of 99(099)
                fileZeros = '0' * (len(str(len(os.listdir('.')))) - len(str(fileNumber + 1))) # len(next(os.walk('.'))[2])

                                
                # for files
                # deletes the dot at the start of the filetype if there is one
                fileExt = filename[(len(filename)-4):].replace('.','')
                
                # filename is the original name of our selected files , after the comma(,) is what it should be renamed to
                # renameWith adds the title
                # str(zeros) + str(fileNumber) adds the corresponding file number
                # '.' + fileExt adds the correct file format       
                os.rename(filename, renameWith + str(fileZeros) + str(fileNumber) + '.' + fileExt)
           

if renamed <= 0:
    print('No files have matched the keywords. Finished renaming 0 items')
elif renamed == 1:
    print('Finished renaming ' + str(renamed) + ' item')
else:
    print('Finished renaming ' + str(renamed) + ' items')
