fhand = open('mbox-short.txt')
for line in fhand:
	line = line.rstrip()
	if not line.startswith('From'):continue
	words = line.split()
	words = line.append()
	print words