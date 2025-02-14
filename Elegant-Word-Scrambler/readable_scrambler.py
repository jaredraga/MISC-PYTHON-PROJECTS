# Author: Jared I. Raga ©2018
# Email: jir@gmail.com
# Beginning  Date: 11/14/18 12:30PM
# Completion Date: 
# Program Name: Readable Word Scrambler
# Program Ver.: 1.0

import random

def scrambler(text):
	list_text = list(text)
	scrambled_word = ''

	already_chosen = []
	while True:
		# Choose a random number in the list except 
		# the first and last numbers
		list_number = random.randint(1, len(list_text)-2)
		
		if len(already_chosen) == len(list_text)-2:
			if scrambled_word == text:
				already_chosen = []
				scrambled_word = ''
				#TODO: how to not result in non-randomized
			else:
				break
		elif list_number in already_chosen:
			continue
		else:
			random_letter = list_text[list_number]
			scrambled_word += random_letter
			already_chosen.append(list_number)

	print(already_chosen)
	return (list_text[0] + scrambled_word + list_text[len(list_text)-1])

	

text = 'break'

while True:
	scrambled = scrambler(text)

	print(scrambled)

	input()