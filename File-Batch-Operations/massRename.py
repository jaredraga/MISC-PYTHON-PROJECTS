#!/usr/bin/env python3
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

#Update: 6/12/18 9:15AM
#Added the smart prompt. Knows if there are only files or only directories
#and it won't number the file/dir if there is only 1 file/dir to rename

#Bug: 6/12/18 10:15AM
#So I've succesfully implemented my Updates, they ran very smoothly with no more errors
#but the number nine still has a problem with its 0s

#Bug: 6/12/18 10:25AM
#So I've fixed the bug that makes the code count files that doesn't match our keyword...
#but with that, it gave birth to another bug that repeats the input prompt over and over again.

#Update: 6/12/18 2:36PM
#I've succesfully fixed the bug that makes the code repeat the input prompt
#but the 0 and 9 problem is still there
import os, os.path

#BIG UPDATE 6/12/18 3:05PM:
#I've fixed the 0 and 9 BUUUUG!!! (Finally, after long hours of hard work)
#I just hacked together a script that does the job but it is fixed!!!!

# select all files with the provided keywords
keyword = input('Files with keywords to rename(e.g:dog jpeg txt):')
keyword = keyword.split()

# rename all selected files with the same title
print('Number will get added after title.')
renameWith = input('Rename with title :')

# format of files being renamed 
# $Expired: replaced with fileExt = filename[(len(filename)-4):].replace('.','')
# renameWithExt = input('Files to rename format (e.g.: \'txt,jpg,mp3\'):') 

# set file numbering to start at arranged value
numberOfFiles = 0
for files in os.listdir('.'):
    if os.path.isfile(files):
        for mask in keyword:
            if mask in files:
                numberOfFiles = numberOfFiles + 1
                # lol wtf. that works, apparently
                if numberOfFiles == 2:
                    fileNumber = input('Begin renaming files at number:')
                    fileNumber = int(fileNumber) - 1
                    break
                    
    
    
# set directory numbering to start at arranged value
numberOfDirs = 0
for dirs in os.listdir('.'):
    if os.path.isdir(dirs):
        for mask in keyword:
            if mask in dirs:
                numberOfDirs = numberOfDirs + 1
                # lol wtf. that works, apparently
                if numberOfDirs == 2:
                    dirNumber = input('Begin renaming dirs at number:')
                    dirNumber = int(dirNumber) - 1
                    break

# counts the renamed files and directories
numberOfRenamedFiles = 0
numberOfRenamedDirs = 0

# this reiterates for every file or folder in the directory
for filename in os.listdir('.'):        
    
    # this runs for every keyword in the keyword list  	
    for mask in keyword:
        
        # if the keyword is in the name of the file/folder , that's only where it should start counting(cycle) the numbers , it should not count the directories/files that's not selected by us
        if mask in filename:            
            
            # if the keyword it matches is a file
            if os.path.isfile(filename):   
                                                                                           
                # deletes the dot at the start of the filetype if there is one
                fileExt = filename[(len(filename)-4):].replace('.','')
                
                # if there is only a single file to rename; it doesn't need to number it
                if numberOfFiles == 1:
                    os.rename(filename, renameWith + '.' + fileExt)             
                 
                # else, if the number of files is greater than 1; it numbers the files                 
                else:
                    # adds one to the the file number everytime we rename a single file
                    fileNumber = fileNumber + 1
                    
                    # my hacked-together script to fix the 09 bug
                    if str(fileNumber).startswith('9'):
                        for char in str(fileNumber):                            
                            if char == '9': 
                                fileZeros = '0' * ((len(str(len(os.listdir('.')))) - len(str(fileNumber + 1))) + 1)
                            elif char != '9':
                                fileZeros = '0' * (len(str(len(os.listdir('.')))) - len(str(fileNumber + 1))) # len(next(os.walk('.'))[2])
                                break    
                    else:
    
                        # configures how many zeros to put depending on the total number of files
                        # len(os.listdir('.') counts how many files there are. in the directory
                        # len(str(os.listdir('.'))) counts the characters of the number of files 100 == 3 characters, 20 == 2 characters
                        # len(str(cycle + 1)) subtracts the zeros based on the character count of the file number , if 100 is the max there should be NO zero in front of 100(0100), but there should be a zero in front of 99(099)
                        fileZeros = '0' * (len(str(len(os.listdir('.')))) - len(str(fileNumber + 1))) # len(next(os.walk('.'))[2])

                    
                    # filename is the original name of our selected files , after the comma(,) is what it should be renamed to
                    # renameWith adds the title
                    # str(zeros) + str(fileNumber) adds the corresponding file number
                    # '.' + fileExt adds the correct file format       
                    os.rename(filename, renameWith + str(fileZeros) + str(fileNumber) + '.' + fileExt)

                                     
                numberOfRenamedFiles = numberOfRenamedFiles + 1
            
            # if the keyword it matches to rename is a directory/folder:
            else:
                
                # if there is only one directory to rename; it doesn't need to number it
                if numberOfDirs == 1:   
                    os.rename(filename, renameWith)
                                              
                # else, if the number of directory is greater than 1; it numbers them
                else:               
                    
                    # adds to the number for every file we rename
                    dirNumber = dirNumber + 1
                    
                                       
                    if str(dirNumber).startswith('9'):
                        for char in str(dirNumber):                            
                            if char == '9': 
                                dirZeros = '0' * ((len(str(len(os.listdir('.')))) - len(str(dirNumber + 1))) + 1)
                            elif char != '9':
                                dirZeros = '0' * (len(str(len(os.listdir('.')))) - len(str(dirNumber + 1))) # len(next(os.walk('.'))[2])
                                break
                    else:
                        # adds the zeros for the numbering
                        dirZeros = '0' * (len(str(len(os.listdir('.')))) - len(str(dirNumber + 1))) # len(next(os.walk('.'))[2])

                    # we don't preserve the file extension because a directory doesn't have a file extension in the first place
                    os.rename(filename, renameWith + str(dirZeros) + str(dirNumber))
               
               
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
