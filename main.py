# Throws words from 'words.txt'
# TXT File From the github project https://github.com/dwyl/english-words

from os import path
from functools import reduce

# Word length + 1 for spacer
MAX_SIZE = 10

def load_words(filename):
  valid_words = []
  with open(filename) as word_file:
    for l in word_file:
      valid_words.append(l[:-1])
  return valid_words
  
def spaceout(word):
	return word + " "*(MAX_SIZE-len(word))

def find_compatible_word(letters):
  compatible_words = []
  for word in word_list_file:
  	if letters in word and len(word) < MAX_SIZE:
  		compatible_words.append(word)
  return compatible_words
  
def remove_word_from_list(root_word, word_list):
	for word in word_list:
		if root_word in word:
			#print("testing: "+ root_word + " -- " + word)
			word_list.remove(word)
  
def shorten_word_list(word_list):
	new_list = []
	tmp_word_list = list(word_list)
	for test_root_word in tmp_word_list:
		possible_base_word = test_root_word[:-1]
		tmp_word_list.remove(test_root_word)
		
		remove_word_from_list(possible_base_word, tmp_word_list)
		remove_word_from_list(possible_base_word, new_list)

		new_list.append(test_root_word)
	return new_list
	

# Main

word_list_file = load_words("words.txt")

while(True):
	letters = input("\nAvailable letters (ie. adhs): ")
	words = find_compatible_word(letters)
	#words = shorten_word_list(words)

	print(f"Found {len(words)} words:")
	if len(words) > 0:
		words.reverse()
		print(reduce(lambda a, b: f"{spaceout(b)}{a}", words))


