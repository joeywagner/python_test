# Use words.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
file = fh.read()
upper = file.upper()
print upper.strip()