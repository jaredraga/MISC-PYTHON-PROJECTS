import os, os.path
files = 0
dirs = 0
for item in os.listdir('.'):
    if os.path.isfile(item):
        files = files + 1
    elif os.path.isdir (item):
        dirs = dirs + 1

print('Files:' + str(files))
print('Folders:' + str(dirs))
