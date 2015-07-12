fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
	tab = line.rstrip('\n')

	lst.append(tab)

print lst
for i in lst:
	print i.split()

fh.close()