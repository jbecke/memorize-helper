# memorize.py {input csv file} {reverse flag, 1 or 0}
# By Jacob Beckerman, jacob dot beckerman at gmail dot com
# Reverse flag = 1: will switch memorizing key->value to value->key

# Takes input from a text file in the form:
#	key, value
#	key, value
#	key, value
#	etc...

import sys
import fileinput

file = sys.argv[1]
rflag = int(sys.argv[2])
wrong_list = set([])

for line in fileinput.input(file):
	tokenized = line.split(",")
	key = tokenized[0].strip()
	value = tokenized[1].strip()
	if len(tokenized) > 2:
		print("ERROR: Only one comma per line")
	elif rflag == 0:
		while True:
			print(key)
			guess = input().strip()
			if guess == value:
				print("_/\n\n")
				break
			else:
				wrong_list.add(key)
	elif rflag == 1:
		while True:
			print(value)
			guess = input().strip()
			if guess == key:
				print("_/\n\n")
				break
			else:
				wrong_list.add(value)
	else:
		print("ERROR: reverse flag must be 0 or 1")
		exit()

for i in wrong_list:
	print("\n\nDone! The ones you got wrong were:")
	print(i)