# Author: Jared I. Raga
# Date of Beginning: 7/20/18 1:30PM
# Date of Completion: 7/20/18 7:30PM

import random
import time
import sys

def main():
	CONSONANTS = 'b c d f g h j k l m n p q r s t v w x y z'.split()
	VOWELS = 'a e i o u'.split()

	num_of_rendered_accounts = 0
	NAMES_TO_GENERATE = 1000
	five_names = ''
	startTime = time.time()
	while True:
		max_random_number_of_characters = random.randint(3,9) # Max number of letters for the name is 9(Note: compound CONSONANTS only count as one character)

		# Randomly choose if the first letter(s) should be a vowel or a consonant
		if random.randint(0,1) == 0:
			first_vowel_or_consonant = 'vowel'
		else:
			first_vowel_or_consonant = 'consonant'

		# If VOWEL
		if first_vowel_or_consonant == 'vowel':
			# Random vowel for the first letter
			first_letter = random.choice(VOWELS)			

		# If CONSONANT
		else:
			# Randomly choose if first letter(s) should be a consonant or compound consonant
			if random.randint(0,1) == 0:
				first_letter = random.choice(CONSONANTS) # consonant
			else:
				compound_consonant = compound_consonant_renderer(CONSONANTS) # compound consonant
				first_letter = compound_consonant

		# CAPITALIZING THE FIRST LETTER
		first_letter = capitalize(first_letter)

		if len(first_letter) > 1:
			previous_previous_letter_figure = letters_figure(first_letter[0], CONSONANTS, VOWELS)
			previous_letter_figure = letters_figure(first_letter[1], CONSONANTS, VOWELS)
		else:
			previous_previous_letter_figure = ''
			previous_letter_figure = letters_figure(first_letter, CONSONANTS, VOWELS)
			
		# CHOOSING SECOND LETTER
		# If first letter is vowel: second letter could be vowel or consonant
		if previous_letter_figure == 'vowel':		
			second_letter = random.choice(VOWELS + CONSONANTS)


		
		# If first letter is consonant: second letter should be vowel
		elif previous_letter_figure == 'consonant':
			second_letter = random.choice(VOWELS)
	
		previous_letter_figure = letters_figure(second_letter, CONSONANTS, VOWELS)

		previous_letter = second_letter
		
		if len(first_letter) > 1:
			previous_previous_letter = first_letter[1]
			previous_previous_letter_figure = letters_figure(first_letter[0], CONSONANTS, VOWELS)
		else:
			previous_previous_letter = first_letter.lower()
			previous_previous_letter_figure = letters_figure(first_letter, CONSONANTS, VOWELS)

		rendered_name = first_letter + second_letter
		num_of_rendered_letters = 2

		#print('First Letter Figure:' + previous_previous_letter_figure)
		#print('Second Letter Figure:' + previous_letter_figure)

		# RENDERING THE FOLLOWING LETTER(S)
		while num_of_rendered_letters <= max_random_number_of_characters:

			# If last two letters are VOWELS
			#if previous_letter_figure == 'vowel' and previous_letter_figure == previous_previous_letter_figure:
				#rendered_letter = random.choice(CONSONANTS) # Choose random consonant					

			if previous_letter_figure == 'vowel':
				if random.randint(0, 1) == 0:
					rendered_letter = random.choice(CONSONANTS)
				else:
					rendered_letter = compound_consonant_renderer(CONSONANTS)
								
			# If previous two letters are CONSONANT
			#if previous_letter_figure == 'consonant' and previous_letter_figure == previous_previous_letter_figure:
				#rendered_letter = random.choice(VOWELS)

			elif previous_letter_figure == 'consonant':
				rendered_letter = random.choice(VOWELS)# + CONSONANTS)
			
			if len(rendered_letter) > 1:
				previous_previous_letter_figure = 'consonant'
				previous_letter_figure = 'consonant'
				previous_previous_letter = rendered_letter[0]
				previous_letter = rendered_letter[1]

			else:
				previous_previous_letter_figure = previous_letter_figure
				previous_letter_figure = letters_figure(rendered_letter, CONSONANTS, VOWELS)
				previous_previous_letter = previous_letter
				previous_letter = rendered_letter		

			rendered_name += rendered_letter

			num_of_rendered_letters = len(rendered_name)

			if num_of_rendered_letters >= max_random_number_of_characters:
				break

			#print(previous_letter_figure)
			

		#print('First letter:' + first_letter)
		#print('Second letter:' + second_letter)
		
		num_of_rendered_accounts += 1   

		rendered_score = random.randint(3, 999999999)


		# Dynamic Printing w/ Score
		#sys.stdout.write("\r%s" % 'Rendered Accounts:' + str(num_of_rendered_accounts) + ' - ' + rendered_name + ' ' * (10 - len(rendered_name)) + str(rendered_score)) 
		#sys.stdout.flush()

		# Dynamic Printing w/out Score
		sys.stdout.write("\r%s" % 'Rendered Accounts:' + str(num_of_rendered_accounts) + ' - ' + rendered_name)
		sys.stdout.flush()
		
		# Writing Names + Score to a .txt
		#with open('rendered accounts.txt','a+') as f:
			#f.writelines(rendered_name + ' ' * (10 - len(rendered_name)) + str(rendered_score))
			#f.writelines('\n')
		
		# Writing Names Only to a .txt
		#with open('mule_names.txt','a+') as f:
			#f.writelines(rendered_name)
			#f.writelines('\n')

		# Writing Names without Newlines to a .txt
		#with open('for dynamic window.txt','a+') as f:
			#f.writelines(rendered_name + ' ')

		# Printing w/ Score
		#print(rendered_name + ' ' * (15 - len(rendered_name)) + str(rendered_score))
		
		# Print Name Only
		#print(rendered_name)
		
		# Stop for Sec
		#time.sleep(0.8)

		# Limit Generation to #
		if num_of_rendered_accounts == NAMES_TO_GENERATE:
			endTime = time.time()
			elapsedTime = str(endTime - startTime)
			for i in range(len(elapsedTime)):
				if elapsedTime[i] == '.':
					elapsedTime = elapsedTime[:i+4]
					break
			print('\nTook %s second(s) to generate %s names.' %(elapsedTime, NAMES_TO_GENERATE))
			break
		
		# Print 5 Names per Line
		#five_names += rendered_name + ' ' * (13 - len(rendered_name))
		#if num_of_rendered_accounts == 5:
			#print(five_names)
			#num_of_rendered_accounts = 0
			#five_names = ''
			#input()			

		# Pressing enter to continue
		#input()

def compound_consonant_renderer(CONSONANTS):
	universal_pairs = 'h l r w'.split()
	
	former = ''
	latter = ''
	while True:
		former = random.choice(CONSONANTS)
		latter = random.choice(CONSONANTS)
		
		if former != latter:
			break

	return former + latter

def capitalize(word):
	if len(word) > 1:
		word = word[0].upper() + word[1:]
	else:
		word = word.upper()
	return word

def letters_figure(letter, CONSONANTS, VOWELS):
	if letter.lower() in CONSONANTS:
		return 'consonant'
	elif letter.lower() in VOWELS:
		return 'vowel'

if __name__ == '__main__':
	main()




