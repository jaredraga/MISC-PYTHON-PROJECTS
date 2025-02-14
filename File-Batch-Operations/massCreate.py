# title pattern of files
title = input('Title of files to create:')

# number of files to create
filesToCreate = input('How many files to create:')

# filetype of the files to be created
fileType = input('Filetype(txt, jpeg, docx):')

for i in range(1, (int(filesToCreate) + 1)):
    
    # configures how many zeros to put depending on the total number of files
    # if the number of files to create is 100 there should be NO zero in front of it (0100), but there should be a zero in front of 99(099)
    zeros = '0' * (len(filesToCreate) - len(str(i)))
    
    # title + zeros + str(i) joins the title plus the correct file number(i)
    # '.' + fileType assigns the filetype to be created
    # open('w+') assigns the permission to write and create a file if it doesn't already exist    
    open(title + zeros + str(i) + '.' + fileType, 'w+') 