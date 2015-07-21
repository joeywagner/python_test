fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
count = 0
counts = dict()
for line in fh:
	line = line.rstrip()
	words = line.split()
	if words ==[] :continue
	if words[0] !='From':continue
	counts[words] = counts.get(words,0) + 1
		
	print words[1]

	
		#counts[word] = counts.get(word,0) + 1
		#print "bang"

	

	

#print "There were", count, "lines in t e file with From as the first word"