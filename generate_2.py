# Load text, prompt for first word, and generate text using a digram (two word)-based Markov chain

# Note: this should eventually prompt for two words

import random
from sys import stdout, exit

# grab the word data from cleaned_shakespeare.txt
f = open("text_sources/cleaned_shakespeare.txt", "r")
stdout.write("Loading text...\n")
words = []
for line in f:
	vals = line.split()
	for w in vals:
		words.append(w)
stdout.write("Done.\n")


in_text = raw_input("Enter your starting words, separated by space: ")
if len(in_text.split()) < 2:
	exit("There entered text is invalid. Exiting...")
prev_word = in_text.split()[0]
current_word = in_text.split()[1]
r = random.SystemRandom()
while True:
	if exit == "quit" or exit == "q":
		break
	indices = []
	for i in range(len(words)):
		if (words[i] == current_word and i == 0) or (words[i] == current_word and words[i-1] == prev_word):
			indices.append(i)
	next_index = 0
	if len(indices) == 0:
		next_index = r.randint(0, len(words)-1)
		#stdout.write("_")
	else:
		next_index = indices[r.randint(0, len(indices)-1)]
	if next_index == len(words)-1:
		next_index = r.randint(0, len(words)-1)
	if len(indices) == 1:
		pass
		#stdout.write("+")
	prev_word = current_word
	current_word = words[next_index+1]
	#stdout.write(" " + str(len(indices)) + " options; chose ")	
	stdout.write(current_word + " ")
	#stdout.write(current_word + "\n")
	stdout.flush()
	# wait until Enter is pressed
	#raw_input()
