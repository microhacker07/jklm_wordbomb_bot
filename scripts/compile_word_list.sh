curl $(cat sources.txt) > rough.txt
tr A-Z a-z < rough.txt | sort | uniq > words.txt
