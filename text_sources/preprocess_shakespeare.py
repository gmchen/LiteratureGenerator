import re

f = open("shakespeare.txt", 'r')

lines = []

for line in f:
	lines.append(line)

# remove the header and footer Gutenberg lines
lines = lines[170:124368]

# Remove thing in square brackets, which are assumed to be stage directions
in_bracket = False
index = 0
while index < len(lines):
	line = lines[index]
	if "[" in line and "]" in line:
		lines[index] = line[0:line.find('[')] + line[line.find(']')+1:]
		line = lines[index]
	elif "[" in line:
		lines[index] = line[0:line.find('[')]
		in_bracket = True
		index = index + 1
		continue
	if in_bracket:
		if "]" in line:
			lines[index] = line[line.find(']')+1:]
			in_bracket = False
		else:
			del lines[index]
			index = index - 1
	index = index + 1

for i in range(len(lines)):
	# Many lines start with "Name.", which we would like to remove.
	line_match = re.match("^[A-Za-z]*\. (.*)$", lines[i])
	if line_match:
		lines[i] = line_match.group()
	else:
		# There lines that start with names looking like "ANTIPHOLUS OF SYRACUSE." - we can only really catch this one for the books where names are all caps.
		line_match = re.match("^([A-Z]* )*[A-Z]*\. (.*)$", lines[i])
		if line_match:
			lines[i] = line_match.groups()[-1]

# Remove all lines containing "by William Shakespeare"
for i in reversed(range(len(lines))):
	if "by William Shakespeare" in lines[i]:
		del lines[i]

words = []
for line in lines:
	vals = line.split()
	for w in vals:
		words.append(w)

for i in reversed(range(len(words))):
	# remove anything that contains no alphabetical letter
	if re.match("^[^A-Za-z]*$" ,words[i]):
		del words[i]
		continue
	# remove anything that contains more than one capital letter. Note that this will delete all values in the Gutenberg messages between works.
	num_caps = 0
	for c in words[i]:
		if re.match("[A-Z]", c):
			num_caps = num_caps + 1
	if num_caps > 1:
		del words[i]
		continue
	# remove anything with Exeunt in it.
	if "Exeunt" in words[i]:
		del words[i]
		continue
	# remove anything with Exit - this shows up, like, 900 times as a stage direction
	if "Exit" in words[i]:
		del words[i]
		continue
	# remove all punctuation except .,;:'"-!?
	for c in words[i]:
		if re.match("[^A-Za-z.,;:'\"\-!?]", c):
			words[i] = words[i].replace(c, "")

outfile = open("cleaned_shakespeare.txt", 'w')
for w in words:
	outfile.write(w + " ")
