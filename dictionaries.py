#Dictionaries
purse = dict()
purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 75
print purse

print purse['candy']

purse['candy'] = purse['candy'] + 2
print purse

#Lists maintain order dictionaries do not maintain order

#Dictionary literals(Constants)
jjj = {'chuck' : 3, 'fred': 42, 'jan': 100}
print jjj


ooo ={}
print ooo

#Many counters with a dictionary
ccc = dict()
ccc['csev'] = 1
ccc['cwen'] = 1
print ccc
ccc['cwen'] = ccc['cwen'] + 1
print ccc

#When we see a new name
counts = dict()
names = ['csev','cwen','csav', 'zqian', 'cwen']
for name in names:
	if name not in counts:
		counts[name] = 1
	else:
		counts[name] = counts[name] + 1
print counts

#The get method for dictionary
if name in counts:
	print counts[name]
else:
	print 0

print counts.get(name,0)#this encapsulates the above if else statement

#Simplified counting with get()
counts = dict()
names = ['csev','cwen','csev','zqian','cwen']
for name in names:
	counts[name] = counts.get(name,0) + 1
print counts

#Counting Pattern
counts = dict()
print 'Enter a line text:'
#the clown ran after the car and the car ran into the tent and the tent fell down on the clown and the car
line = raw_input('')
words = line.split()
print 'Words:', words

print 'Counting.....'
for word in words:
	counts[word] = counts.get(word,0) + 1

print 'Counts', counts

#Definite loops and dictionaries
counts = { 'chuck': 1 , 'fred' : 42, 'jan' : 100}
for key in counts:
	print key, counts[key]

#Retrieving a list of Keys and values
jjj = {'chuck' : 3, 'fred': 42, 'jan': 100}
print list(jjj)

print jjj.keys()
print jjj.values()
print jjj.items()

#Bonus: Two iteration variables
jjj = {'chuck' : 3, 'fred': 42, 'jan': 100}
for aaa, bbb in jjj.items():
	print aaa,bbb




#################################################
name = raw_input("Enter a file Name:")
handle = open(name, 'r')
text = handle.read()
words = text.split()

counts = dict()
for word in words:
	counts[word] = counts.get(word,0) + 1

bigcount = None
bigword = None
for word,count in counts.items():
	if bigcount is None or count > bigcount:
		bigword = word
		bigcount = count

print bigword,bigcount







