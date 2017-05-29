# memorize.py {input csv file} {reverse flag, 1 or 0}
# By Jacob Beckerman, jacob dot beckerman at gmail dot com
# Reverse flag = 1: will switch memorizing key->value to value->key
# Type q tomove on

# Takes input from a text file in the form:
#	key, value
#	key, value
#	key, value
#	etc...

import sys
import fileinput

file = sys.argv[1]
rflag = int(sys.argv[2])
to_test = {}

# Get everything into a dictionary
for line in fileinput.input(file):
	tokenized = line.split(",")
	key = tokenized[0].strip()
	value = tokenized[1].strip()
	if len(tokenized) > 2:
		print("ERROR: Only one comma per line")
		exit(1)
	to_test[key] = value

def test(to_test):
	next_test = {}
	wrong_list = set([])
	for key, value in to_test.items():
		if rflag == 0:
			while True:
				print(key)
				guess = input().strip()
				if guess == value:
					print("_/\n\n")
					break
				elif guess == 'q':	# give up
					print("X\n\n")
					wrong_list.add(key)
					next_test[key] = value
					break
				elif guess == 'a':	# give answer
					print(value)
				elif guess == 'c':	# accept answer as right
					print("_/\n\n")
					break
				elif guess == 'exit':	# accept answer as right
					print("\n\nDone! The ones you got wrong were:")
					for i in wrong_list:
						print(i)
					exit()
				else:
					wrong_list.add(key)
					next_test[key] = value
		elif rflag == 1:
			while True:
				print(value)
				guess = input().strip()
				if guess == key:
					print("_/\n\n")
					break
				elif guess == 'q':
					print("X\n\n")
					wrong_list.add(value)
					next_test[key] = value
					break
				elif guess == 'a':
					print(key)
				elif guess == 'c':
					print("_/\n\n")
					break
				elif guess == 'exit':	# accept answer as right
					print("\n\nDone! The ones you got wrong were:")
					for i in wrong_list:
						print(i)
					exit()
				else:
					wrong_list.add(value)
					next_test[key] = value

	print("\n\nDone! The ones you got wrong were:")
	for i in wrong_list:
		print(i)
	print("\n\n")
	if len(next_test) != 0:
		test(next_test)


test(to_test)