keyword = 'bacon'.split()
keyword = str(keyword).replace('[','')
keyword = str(keyword).replace(']','')
keyword = str(keyword).replace("'","")

print('No file or directory have matched the keyword/s:' + '"' + str(keyword) + '"')
