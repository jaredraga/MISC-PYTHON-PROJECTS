# Author: Jared I. Raga
# Date of Beginning:  7/20/18 12:15AM
# Date of Completion: 7/20/18 12:40AM

# I wasn't doing anything as I've quit going to school, so I figured I might just do create this script.
# Retrieved the names from the Teacher's Table(I took a pic of it when nobody was looking :))

import random

# Store the student subjects to a list from a text file
student_list = []
with open('student_list.txt','r') as f:
	student_list = f.readlines()

rank = 1
students_chosen = []
while len(student_list) != len(students_chosen): 
	random_student = random.choice(student_list) # Choose a random student from the list
	
	 # Store the students that are already chosen to a list
	if random_student not in students_chosen:
		students_chosen.append(random_student)
		print(str(rank) + '. ' +random_student)

		# Open a text file and create one if it doesn't exist
		with open('result.txt','a+') as f: 
			f.writelines(str(rank) + '. ' +random_student)
			f.writelines('\n')

		rank += 1
