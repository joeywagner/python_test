fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh.read().split():
	
	if line not in lst:
		lst.append(line)


lst.sort()

print lst

	
	
	
	


	






	
	
	


		


	



