# Author: Jared I. Raga ©2018
# Email: jir@gmail.com
# Beginning  Date: 7/20/18 12:45AM
# Completion Date: 7/20/18  2:05AM
# Program Name: Console-Based Dynamic Window


# Author: Jared I. Raga
# Date of Beginning: 7/20/18 12:45AM
# Date of Completion: 7/20/18 2:05AM

# I'm happy that I've done it! I don't need to go to school to learn programming, I could just learn it by myself!

import time
time.sleep(0.5)
print('''Console-Based Dynamic Window

Please follow the instructions to get the best out of this software.

The non-permitted use of this software in any means possible is prohibited.
Please contact the author for more information.
You can contact me at: jir@gmail.com
Author: Jared I. Raga ©2018

Email: jir@gmail.com
Beginning  Date: 7/20/18 12:45AM
Completion Date: 7/20/18  2:05AM
Program Name: Console-Based Dynamic Window
''')
time.sleep(1)
print('''
Provide your items below.
Seperate your items by spaces.
i.e. Items: Icemete Zlugic Emubu Lwuvu Kidocen Fetaf Wowo
''')

		
while True:
	# 

	test_subjects = input('Items: ')
	print()

	# Store the test subjects to a list
	test_subjects = test_subjects.split()

	LEFT_WINDOW_BORDER  = '** '
	RIGHT_WINDOW_BORDER = ' **'

	# Get the length of longest subject to set the table width
	table_width = len(LEFT_WINDOW_BORDER) + len(RIGHT_WINDOW_BORDER)
	longest = 0
	for test_subject in test_subjects:
		# Length of subject + Length of subject number + Length of Window Borders
		if len(test_subject) > longest:
			longest = len(test_subject)
	table_width += longest
	print(table_width)

	# Add the necessary elements to the row
	rows = []
	sub_number = 0
	for test_subject in test_subjects:

		# clear previous row contents
		row = ''
		sub_number += 1
		sub_number_with_dot = str(sub_number) + '. '
		
		# Left window border
		row += LEFT_WINDOW_BORDER

		# Subject number
		row += sub_number_with_dot
		
		# Add the SUBJECT
		row += test_subject 
		
		# Add the table width
		row += ' ' * (table_width - len(test_subject) - len(sub_number_with_dot))
		
		# Right window border
		row += RIGHT_WINDOW_BORDER
		
		rows.append(row)
		
	# Top of the Window
	print('-' * (table_width + 7))
	for row in rows:
		print(row)
	print('-' * (table_width + 7))
	# Bottom of the Window

	print()
	print('+' * (table_width + 7))
	print()
