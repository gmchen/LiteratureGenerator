# Load text, prompt for first word, and generate text using a unigram (one word)-based Markov chain

import random
from sys import stdout

# grab the word data from cleaned_shakespeare.txt
f = open("text_sources/cleaned_shakespeare.txt", "r")
stdout.write("Loading text...\n")
words = []
for line in f:
	vals = line.split()
	for w in vals:
		words.append(w)
stdout.write("Done.\n")

current_word = raw_input("Enter a starting word: ")
r = random.SystemRandom()

while True:
	if exit == "quit" or exit == "q":
		break
	indices = []
	for i in range(len(words)):
		if words[i] == current_word:
			indices.append(i)
	next_index = 0
	if len(indices) == 0:
		next_index = r.randint(0, len(words)-1)
		stdout.write("_")
	else:
		next_index = indices[r.randint(0, len(indices)-1)]
	if next_index == len(words)-1:
		next_index = r.randint(0, len(words)-1)
	if len(indices) == 1:
		pass
		#stdout.write("+")
	current_word = words[next_index+1]
	stdout.write(current_word + " ")
	stdout.flush()
	# wait until Enter is pressed
	# raw_input()
	
