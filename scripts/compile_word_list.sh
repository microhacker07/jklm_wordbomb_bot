#!/bin/sh

curl $(cat sources.txt) > rough.txt
cat additional_words.txt >> rough.txt

# Pain in the ass to why there are doubles in a file after running uniq
# But this removes carraige returns that make some words 'unique'
tr -d '\r' < rough.txt | tr [:upper:] [:lower:] | sort | uniq > words.txt
