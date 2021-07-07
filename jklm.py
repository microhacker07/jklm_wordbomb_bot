import argparse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import words
import random

def delayed_type(element, text):
  try:
    element.clear()
    for t in text:
      element.send_keys(t)
      sleep(0.1)
    element.send_keys(Keys.RETURN)
  except:
    print(f"{username} was unable to enter {text}")


username = "guest69420"
room_code = "NULL"

parser = argparse.ArgumentParser(description='Bot for wordbomb from jklm.fun')
 
# Adding optional argument
parser.add_argument('room_code', help='room code for jklm.fun')
parser.add_argument('-n', '--name', help="bot's username")
 
# Read arguments from command line
args = parser.parse_args()
 
room_code = args.room_code
if args.name != None:
  username = args.name


driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('https://jklm.fun/' + room_code)
assert "JKLM" in driver.title

# Nickname field
nick_elem = driver.find_element_by_class_name("nickname")
delayed_type(nick_elem, username)
print(f"{username} has logged on")

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
    sleep(2)
    syllable = driver.find_element_by_class_name("syllable").text
    com_words = words.find_compatible_word(syllable, tmp_word_list)

    selected_word = ""
    if len(com_words) > 0:
      selected_word = com_words[int(random.random()*len(com_words))]

    tmp_word_list.remove(selected_word)

    delayed_type(input_elem, selected_word)

driver.close()

