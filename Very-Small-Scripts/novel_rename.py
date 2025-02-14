# B: 8/1/18 12:08PM
# C: 8/1/18 12:20PM

# novel_rename.py - renames the novels' chapters' filenames containing '_' to ' -'

import os

# counts the renamed files
renamed = 0

for filename in os.listdir('.'):
    
    newname = filename.replace('_',' -')

    os.rename(filename, newname)

    print('Renamed %s to %s' % (filename, newname))
    
    renamed += 1
