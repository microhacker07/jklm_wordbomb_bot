import argparse
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from localStorage import LocalStorage
from localStorage import get_image_as_base64
import random
import words
import json

def delayed_type(element, text):
  try:
    element.clear()
    if args.god:
      element.send_keys(text)
    else:
      for t in text:
        element.send_keys(t)
        sleep(random_interval(0, 0.1))
    element.send_keys(Keys.RETURN)
    return True
  except:
    print(f"{username} was unable to enter {text}")
    return False
    
def random_interval(min_val, max_val):
  return min_val + random.random() * (max_val - min_val)
  
def random_int(min_val, max_val):
  return int(random_interval(min_val, max_val))

def random_word(words):
  selected_word = ""
  if len(words) > 0:
    selected_word = words[int(random_interval(0, len(words)))]
  return selected_word


# Arguments

parser = argparse.ArgumentParser(description='Bot for wordbomb from jklm.fun')
 
# Adding optional argument
parser.add_argument('room', help='room code for jklm.fun')
parser.add_argument('-n', '--name', help="bot's username")
parser.add_argument('-m', '--mode', help="different word selection modes (0 is default): 0=random, 1=short, 2=long")
parser.add_argument('-i', '--img', help="url an image")
parser.add_argument('-g', '--god', action='store_true', help='enable "godspeed" mode')
 
# Read arguments from command line
args = parser.parse_args()


# Setup

room_code = args.room

username = "guest69420"

if args.name != None:
  username = args.name

mode = 0

if args.mode != None and (0 <= int(args.mode) <= 2):
  mode = int(args.mode)

from webdriver import driver
driver.implicitly_wait(10)
driver.get('https://jklm.fun/' + room_code)
assert "JKLM" in driver.title

# Nickname field
nick_elem = driver.find_element_by_class_name("nickname")
delayed_type(nick_elem, username)
print(f"{username} has logged on")

if args.img != None:
  sleep(2)
  storage = LocalStorage(driver)

  image = get_image_as_base64(args.img)
  jklmDict = json.loads(storage["jklmSettings"])
  jklmDict["picture"] = image
  storage["jklmSettings"] = json.dumps(jklmDict)
  driver.refresh()


# Change to game iframe
iframe = driver.find_element_by_tag_name("iframe")
driver.switch_to.frame(iframe)

# Syllable text
# driver.find_element_by_class_name("syllable").text

join_elem = driver.find_element_by_class_name("joinRound")
turn_elem = driver.find_element_by_class_name("selfTurn")
input_elem = turn_elem.find_element_by_xpath(".//input")
word_list_file = words.load_words("words.txt")
tmp_word_list = list(word_list_file)

while True:
  sleep(0.2)

  if join_elem.is_displayed() and join_elem.text != '':
    # Join button
    try:
      join_elem.click()
      tmp_word_list = list(word_list_file)
    except:
      print(f"{username} was unable to press join")

  
  if turn_elem.is_displayed() and input_elem.is_displayed():
    sleep(random_interval(1, 2))
    syllable = driver.find_element_by_class_name("syllable").text
    com_words = words.find_compatible_word(syllable, tmp_word_list)

    selected_word = ""
    if mode == 0:
      selected_word = random_word(com_words)
    elif mode == 1:
      words.rate_words(com_words)
      selected_word = com_words[0]
    elif mode == 2:
      words.rate_words(com_words)
      selected_word = com_words[-1]

    if delayed_type(input_elem, selected_word) and selected_word != "":
      tmp_word_list.remove(selected_word)
    elif selected_word == "":
      print(f"{username} could not find a word for {syllable}")

driver.close()

