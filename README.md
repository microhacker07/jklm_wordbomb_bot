# jklm_wordbomb_bot

A project to have a bot play the wordbomb game from [jklm.fun](https://jklm.fun/).
Currently it uses an english dictionary that is compiled from sources that are
apparently used by the game<sup>[reference](https://www.reddit.com/r/BombParty/comments/64fhwy/the_complete_english_bombparty_dictionary/?utm_source=share&utm_medium=web2x&context=3)</sup>.

# Prerequisite

- Python 3
- Selenium

## Selenium

Selenium requires a browser driver to use a browser for automation. [Check it out here](https://www.selenium.dev/documentation/en/getting_started_with_webdriver/)

# Recommended setup

Recommended to install dependencies and run the program in an virtual environment
to prevent version mismatch from global packages.

[Howto from the docs on python's venv](https://docs.python.org/3/library/venv.html)

Install the requirements with:

`pip3 install -r requirements.txt`

Currently this only installs the python module for Selenium

# Game Bot

Run the game bot with:

`python3 jklm.py ROOM`

Where ROOM is the room code the bot can join.

For more options (like custom name) run `python3 jklm.py -h` for more agruments

# Dictionary Bot

Similiar to the game bot:

`python3 dict.py ROOM`

This bot will watch the chat of the lobby and if it find the command `.d`
along with a syllable it will put five _random_ words that contain the
syllable in chat.

Ex:
User types out:

`.d ia`

The bot will return with:

`sequentially, fiducial, appreciates, giantly, potentiality`