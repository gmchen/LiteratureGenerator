import re

f = open("Bible_KJV.txt", 'r')

text = f.read()
pars = text.split("\r\n\r\n")

# Remove other line breaks; strip leading and trailing space
for i in range(len(pars)):
	pars[i] = pars[i].replace("\r\n", " ")
	pars[i] = pars[i].strip()

# Only keep lines starting with number:number
for i in reversed(range(len(pars))):
	match = re.match("^[0-9]+:[0-9]+", pars[i])
	if match is None:
		del pars[i]

# Remove number:number
for i in range(len(pars)):
	nums = re.findall("[0-9]+:[0-9]+", pars[i])
	for n in nums:
		pars[i] = pars[i].replace(n, "")

words = []
for p in pars:
	vals = p.split()
	for v in vals:
		words.append(v)

for i in reversed(range(len(words))):
	if len(words[i]) < 1:
		del words[i]

outfile = open("cleaned_bible.txt", 'w')
for w in words:
	outfile.write(w + " ")
