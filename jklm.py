from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import words

def delayed_type(element, text):
  for t in text:
    element.send_keys(t)
    sleep(0.2)

username = "nat"
room_code = "FCEY"
#room_code = input("Room code: ")

driver = webdriver.Chrome()
driver.get('https://jklm.fun/' + room_code)
assert "JKLM" in driver.title

sleep(2)
# Nickname field
nick_elem = driver.find_element_by_class_name("nickname")
nick_elem.clear()
delayed_type(nick_elem, username)
nick_elem.send_keys(Keys.RETURN)

sleep(4)
# Change to game iframe
iframe = driver.find_element_by_tag_name("iframe")
driver.switch_to.frame(iframe)

# Join button
join_elem = driver.find_element_by_class_name("joinRound")
join_elem.click()

# Syllable text
# driver.find_element_by_class_name("syllable").text

#while True:


#driver.close()

