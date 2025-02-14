#6/2/18 10:45AM:

import os
import shutil


# it's not working
# 6/2/18 2:10PM
# it's working now

# select all files with the selected keyword

keywordSelect = input('Files with keyword to move(e.g.:jpg dogs txt):')
keywordSelect = keywordSelect.split()

# keyword = 'pdf,doc'
# keyword = '\''+keyword+'\''

dest = input('Move to(dir must already exist!):')

for filename in os.listdir('.'):    
    
    for keywords in keywordSelect:
        if keywords in filename:  
            print(filename)  
            shutil.move(filename, dest)
    # keyword = keyword.replace(',', '\'or\'')
                
    # print(keyword)         
    