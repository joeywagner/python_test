#looking inside strings
fruit = 'banana'
letter = fruit[1]
print letter

n =3
w = fruit[n -1]
print w

print 'NEW BLOCK'
#strings have length
fruit = 'banana'
print len(fruit)

print "NEW BLOCK"


#Looping through strings
fruit = 'banana'
index = 0
while index < len(fruit):
	letter = fruit[index]
	print index, letter
	index = index + 1

print "NEW BLOCK"
fruit = 'banana'
for letter in fruit :
	print letter

print 'NEW BLOCK'

#Looping and Counting
word = 'banana'
count = 0
for letter in word:
	if letter == 'a':
		count = count + 1
print count

print 'NEW BLOCK'

#Slicing strings
s = 'Monty Python'
print s[:2]
print s[8:]
print s[:]

print 'NEW BLOCK'

#String Concatenation
a = 'Hello'
b = a + 'There'
print b

c = a + ' ' + 'There'
print c

print 'NEW BLOCK'

#Using in as an operator
fruit = 'banana'
'n' in fruit
'm' in fruit
'nan' in fruit
if 'a' in fruit :
	print 'Found it!'

print 'NEW BLOCK'
# String Comparison
if word == 'banana':
	print 'All right, bananas.'

if word < 'banana':
	print 'Your word,' + word + ', comes before banana.'
elif word > 'banana':
	print 'Your word,' + word + ', comes after banana'
else:
	print 'All right, bananas.'

print 'NEW BLOCK'

#String Library
greet = 'Hello Bob'
zap = greet.lower()
print zap

print greet

print 'Hi There'.lower()

print 'NEW BLOCK'


#############################
stuff = 'Hello world'
type(stuff)
dir(stuff)
stuffcap = stuff.upper()

print stuffcap

print 'NEW BLOCK'

#Searching a String
fruit = 'banana'
pos = fruit.find('na')
print pos
aa = fruit.find('z')
print aa

print 'NEW BLOCK'

#Maring everything upper case
greet = 'Hello Bob'
nnn = greet.upper()
print nnn
www = greet.lower()
print www

print 'NEW BLOCK'



#Search and Replace
greet = 'Hello Bob'
nstr = greet.replace('Bob','Jane')
print nstr

greet = 'Hello Bob'
nstr = greet.replace('o','X')
print nstr


print 'NEW BLOCK'

#Stripping Whitespace
greet = '  Hello Bob  '
greetl = greet.lstrip()
print greetl
greetr = greet.rstrip()
print greetr
greetstrip = greet.strip()
print greetstrip
print 'NEW BLOCK'


#Prefixes
line = 'Please have a nice day'
line.startswith('Please')

line.startswith('p')


#Parsing text
data = 'From joe.wagner@hp.com sat july 1 09:14:44 2015'
atpos = data.find('@')
print atpos

sppos = data.find(' ',atpos)
print sppos
host = data[atpos+1 :sppos]
print host











