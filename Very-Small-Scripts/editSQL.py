#! python3

# editSQL.py -- edits the file 'SQL_Injections.txt'. Removes newlines and tabs. Neatly rewrites the strings in a nice list.

# Beginning: 7/27/18 10:10AM
# Completion:7/27/18 10:20AM
def process_text(filename):
	open(filename,'a+') # this line makes sure the file exists; if it doesn't, it creates the file.
	with open(filename,'r') as f:
		raw_data = f.readlines()

	
	# Stage 1: removing newline and tab characters
	stage_1 = []
	edited = ''
	for line in raw_data:
		edited = line.replace('\n', '')
		edited = edited.replace('\t', '')
		stage_1.append(edited)

	# Stage 2: splitting the strings
	stage_2 = []
	for line in stage_1:
		line_split = line.split()
		for i in range(len(line_split)):
			stage_2.append(line_split[i])

	# Done.

	# Writing the processed text
	with open('New_SQL_Injections.txt','a+') as f:
		for line in stage_2:
			f.writelines(line)
			f.writelines('\n')

data = process_text('SQL_Injections.txt')


