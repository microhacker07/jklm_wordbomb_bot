import argparse

parser = argparse.ArgumentParser(description='Bot for wordbomb from jklm.fun')
 
# Adding optional argument
parser.add_argument('room', help='room code for jklm.fun')
parser.add_argument('-n', '--name', help="bot's username")
parser.add_argument('-g', '--god', action='store_true', help='enable "godspeed" mode')
 
# Read arguments from command line
Args = parser.parse_args()