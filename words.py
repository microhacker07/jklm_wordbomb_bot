# Throws words from 'words.txt'
# TXT File From the github project https://github.com/dwyl/english-words

from os import path

def load_words(filename):
  valid_words = []
  with open(filename) as word_file:
    for l in word_file:
      valid_words.append(l[:-1])
  return valid_words

def find_compatible_word(letters):
  global word_list_file
  compatible_words = []
  for word in word_list_file:
    if letters in word:
      compatible_words.append(word)
  return compatible_words
  
def word_rate_function(bonus_letters):
  def F(word):
    bonus = sum([int(l in word) for l in bonus_letters])
    return len(word) - 2 * bonus
  return F
  
def rate_words(words, bonus_letters):
  sort_func = word_rate_function(bonus_letters)
  words.sort(key=sort_func)

# Main

word_list_file = load_words("words.txt")

if __name__ == "__main__":
  from functools import reduce

  while(True):
    letters = input("\nAvailable letters (ie. adhs): ")
    words = find_compatible_word(letters)
    rate_words(words, ["a", "c"])

    print(f"Found {len(words)} words:")
    if len(words) > 0:
      words.reverse()
      print(reduce(lambda a, b: f"{b} {a}", words))


