from os import path

def load_words(filename):
  valid_words = []
  with open(filename) as word_file:
    for l in word_file:
      line = l[:-1]
      if len(line) <= 30:
        valid_words.append(line)
  return valid_words

def find_compatible_word(letters, word_list):
  compatible_words = []
  for word in word_list:
    if letters.lower() in word.lower():
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
if __name__ == "__main__":
  from functools import reduce

  word_list_file = load_words("words.txt")

  while(True):
    letters = input("\nAvailable letters (ie. adhs): ")
    words = find_compatible_word(letters, word_list_file)
    rate_words(words, ["a", "c"])

    print(f"Found {len(words)} words:")
    if len(words) > 0:
      words.reverse()
      print(reduce(lambda a, b: f"{b} {a}", words))


