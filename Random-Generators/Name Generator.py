# Author: Jared I. Raga ©2018
# Email: jir@gmail.com
# Beginning  Date: 7/20/18
# Completion Date: 7/20/18 10:45PM
# Program Name: Name Generator

import random
import time
import sys
import androidhelper

android = androidhelper.Android()
print('Name Generator')

def main():
	CONSONANTS = 'b c d f g h j k l m n p q r s t v w x y z'.split()
	VOWELS = 'a e i o u'.split()

	while True:
		max_random_number_of_characters = random.randint(3,6) # Max number of letters for the name is 9(Note: compound CONSONANTS only count as one character)

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
			if random.randint(0, 1) == 0:
				second_letter = random.choice(VOWELS)
			else:
				second_letter = random.choice(CONSONANTS)					
		
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
				rendered_letter = random.choice(CONSONANTS)# + VOWELS)
								
			# If previous two letters are CONSONANT
			#if previous_letter_figure == 'consonant' and previous_letter_figure == previous_previous_letter_figure:
				#rendered_letter = random.choice(VOWELS)

			if previous_letter_figure == 'consonant':
				rendered_letter = random.choice(VOWELS)# + CONSONANTS)
			

			previous_previous_letter_figure = previous_letter_figure
			previous_letter_figure = letters_figure(rendered_letter, CONSONANTS, VOWELS)
			previous_previous_letter = previous_letter
			previous_letter = rendered_letter		

			rendered_name += rendered_letter

			num_of_rendered_letters += 1

			#print(previous_letter_figure)
			

		#print('First letter:' + first_letter)
		#print('Second letter:' + second_letter)
		#print(rendered_name)
		android.notify(rendered_name,'Name Generator')


		#num_of_rendered_accounts += 1
		
					
		#sys.stdout.write("\r%s" % rendered_name)
		#sys.stdout.flush()
		
		print(rendered_name)
		start = time.time()
		while True:
			
			sys.stdout.write("\r%s" % str(int(time.time() - start)) + '/3600 seconds elapsed.')
			sys.stdout.flush()
			
			if int(time.time() - start) >= 3600:
				break
			
		    		    		    			
		#input()

def compound_consonant_renderer(CONSONANTS):
	universal_pairs = 'h l r w'.split()
	
	former = ''
	latter = ''
	while True:
		former = random.choice(CONSONANTS)
		latter = random.choice(universal_pairs)
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




