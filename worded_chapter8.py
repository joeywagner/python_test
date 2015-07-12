fhand =open('mbox-short.txt')
for line in fhand:
	line = line.rstrip()
	words = line.split()
	#print words
	if words ==[]:continue
	if words[0] != 'From':continue
	print words[2]
