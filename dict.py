import argparse
from functools import reduce
from webdriver import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import random
import words

def delayed_type(element, text):
  try:
    element.clear()
    element.send_keys(text)
    element.send_keys(Keys.RETURN)
  except:
    print(f"{username} was unable to enter {text}")
    
def random_interval(min_val, max_val):
  return min_val + random.random() * (max_val - min_val)
  
def random_int(min_val, max_val):
  return int(random_interval(min_val, max_val))

# Command Line Agruments


parser = argparse.ArgumentParser(description='Dict bot for wordbomb from jklm.fun')
 
# Adding optional argument
parser.add_argument('room', help='room code for jklm.fun')
parser.add_argument('-n', '--name', help="bot's username")
 
# Read arguments from command line
Args = parser.parse_args()


# Setup

room_code = Args.room

username = "dict"

if Args.name != None:
  username = Args.name


driver.implicitly_wait(10)
driver.get('https://jklm.fun/' + room_code)
assert "JKLM" in driver.title

# Nickname field
nick_elem = driver.find_element_by_class_name("nickname")
delayed_type(nick_elem, username)

input_elem = driver.find_element_by_xpath("//textarea")
word_list = words.load_words("words.txt")

while True:
  sleep(0.25)
  chat = driver.find_elements_by_class_name("text")
  if len(chat) > 0:
    latest_msg = chat[-1].text
    if '.d' in latest_msg and len(latest_msg.split()) > 1:
      syllable = latest_msg.split()[1]
      com_words = words.find_compatible_word(syllable, word_list)
      
      print_length = 5
      if len(com_words) < 5:
        print_length = len(com_words)

      five_random_words = []
      for i in range(print_length):
        ran_word = com_words[int(random_interval(0, len(com_words)))]
        five_random_words.append(ran_word)
        com_words.remove(ran_word)

      if len(five_random_words) > 0:
        text = reduce(lambda a, b: f"{a}, {b}", five_random_words)

      delayed_type(input_elem, text)

driver.close()

