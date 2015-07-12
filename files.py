#New Lines
stuff = 'Hello\nWorld!'
print stuff
stuff = 'X\nY'
print stuff
print len(stuff)

#File Processing
#new lies are at the end of the line

#xfile = open('mboc.txt')
#for line in xfile:
#	print line

#Counting the number of lines in a file
fhand = open('mbox.txt')
count = 0
for line in fhand:
	count = count + 1
print 'Line count',count

#Reading the Whole File
fhand = open('mbox-short.txt')
inp = fhand.read()
print len(inp)
print inp[:20]

#File Processing#

#Searching through a file
fhand = open('mbox-short.txt')
for line in fhand:
	line = line.rstrip()
	if line.startswith('From:')
	print line

#Skipping with continue
fhand = open('mbox-short.txt')
for line in fhand:
	line = line.rstrip()
	#Skip 'uninteresting line'
	if not line.startswith('From:')
		continue
	#Processing our 'intersting' line
	print line


#Searching Through a file (fixed)
fhand = open('mbox-short.txt')
for line in fhand:
	line = line.rstrip()
	if line.startswith('From:'):
		print line

#Skipping with continue
fhand = open('mbox-short.txt')
for line in fhand
	line = line.rstrip()
	#Skip 'unintersting line'
	if not line.startswith('From:'):
		continue
	#Process our intersting line
	print line

#Using in to select lines
fhand = open('mbox-short.txt')
for line in fhand:
	line =line.rstrip()
	if not '@uct.ac.za' in line:
		continue
	print line

#Prompt for File Name
fname = raw_input('Enter the file name: ')
fhand = open(fname)
count = 0
for line in fhand:
	if line.startswith('Subject'):
		count - count +1
print 'There were',count,'subject line in',fname


#Bad File Names
fname = raw_input('Enter the file name: ')
try:
	fhand = open(fname)
except:
	print 'File cannot be opened:',fname
	exit()
count = 0
for line in fhand:
	if line.startswith('Subject'):
		count = count + 1
print 'There were',count,'subject lines in'















