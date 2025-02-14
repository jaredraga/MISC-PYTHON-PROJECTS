# Author: Jared I. Raga ©2018
# Email: jir@gmail.com
# Beginning  Date: 10/?/18
# Completion Date: 10/24/18 8:20PM
# Program Name: Word-based Name Generator
# Program Ver.: 1.0.0

# Generating names by joining two words together from the dictionary.

# Rules:
# 1. Combined words mustn't exceed 10 letters

# Wtf!? It worked on the first try

# Later...
# As it turned out, there are a lot of boring words in the English Dictionary
# So it looks like we won't be using this code after all. LMAO

import random

def load_words():
	with open('words_alpha.txt','r') as word_file:
		word_list = word_file.readlines()

	no_newlines = []
	for i in range(len(word_list)):
		no_newlines.append(word_list[i].replace('\n',''))
	return no_newlines

if __name__ == '__main__':
	english_words = load_words()

	while True:
		first_word = random.choice(english_words)
		second_word = random.choice(english_words)

		if len(first_word + second_word) > 10:
			continue
		else:
			generated_name = first_word.capitalize() + second_word.capitalize()
			print(generated_name)
			input() #Press any key to continue