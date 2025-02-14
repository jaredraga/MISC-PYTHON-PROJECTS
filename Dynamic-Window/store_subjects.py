# Author: Jared I. Raga
# Date of Beginning: 7/20/18 12:45AM
# Date of Completion: 7/20/18 

# Store the test subjects to a list from a text file
test_subjects = []
with open('student_list.txt','r') as f:
	test_subjects = f.readlines()
print(test_subjects)

table_width = 0
for test_subject in test_subjects:
	if len(test_subject) > table_width:
		table_width = len(test_subject)
	
	print(test_subject + ' ' + str(len(test_subject)))
print(table_width)

rows = []
for test_subject in test_subjects:
	row = '- ' + test_subject + ' ' * (table_width - len(test_subject)) + ' -'
	rows.append(row)

print('-' * (table_width + 4))
for row in rows:
	print(row)
print('-' * (table_width + 4))