#List Constants
print[1,24,76]
print['red','yellow','blue']
print['red',24,98.6]
print[1,[5,6],7]
print[]

#Lists and definite loops
friends = ['Joseph','Glenn','Sally']
for friends in friends:
	print 'happy new year!', friends

print 'Done!'

#Looking inside lists
friends = ['joseph','Glenn','Sally']
print friends[1]

#Lists are mutable
fruit = 'Banana'
x = fruit.lower()
print x

lotto = [2,14,26,41,63]
print lotto
lotto[2] = 28
print lotto

#Using the Range function
print range(4)
friends = ['joseph','Glenn','Sally']
print len(friends)
print range(len(friends))

#A tale of two loops
friends = ['joseph','Glenn','Sally']

for friend in friends:
	print 'Happy New Year!', friend

for i in range(len(friends)):
	friend = friends[i]
	print 'Happy New Year', friend

#Concantinating list using +
a = [1,2,3]
b = [4,5,6]
c = a + b
print c

#Lists can be sliced using :
t = [9,41,12,3,74,15]
t = t[1:3]
print t
t = [9,41,12,3,74,15]
t = t[:4]
print t
t = [9,41,12,3,74,15]
t = t[3:]
print t
t = [9,41,12,3,74,15]
t = t[:]
print t


#list methods
x = list()
type(x)
dir(x)

#Building a list from scratch
stuff = list()
stuff.append('book')
stuff.append(99)
print stuff

stuff.append('cookie')
print stuff


#Is something in a List
some = [1,9,21,10,16]
a = 9 in some
print a
b = 15 in some
print b
c = 30 not in some
print c
if c == True:
	print '30 is in the list'
else:
	print ' 30 is not in the list'

#A list is an Ordered Sequence
friends = ['Joseph','Glenn','Sally']
friends.sort()
print friends
print friends[1]

#Built in Functions and list
nums = [3,41,12,9,74,15]
print len(nums)
print max(nums)
print min(nums)
print sum(nums)
print sum(nums)/len(nums)

#Averaging a list
total = 0
count = 0
while True:
	inp = raw_input('Enter a number:')
	if inp == 'done':break
	value = float(inp)
	total = total + value
	count = count + 1
average = total / count
print 'average', average

#######
numlist = list()
while True:
	inp = raw_input('Enter a number')
	if inp == 'done': break
	value = float(inp)
	numlist.append(value)

average = sum(numlist) / len(numlist)
print 'Average', average

#Best Friends Stings and Lists
abc = 'With three words'
stuff = abc.split()
print stuff
print len(stuff)
print stuff[0]
print stuff
for w in stuff:
	print w

#Split spaces
line = 'A lot             of spaces'
etc = line.split()
print etc

line = 'first;second;third'
thing = line.split()
print thing
print len(thing)
thing = line.split(';')
print thing
print len(thing)

#Finding data
fhand = open('mbox-short.txt')
for line in fhand:
	line = line.rstrip()
	if not line.startswith('From'):continue
	words = line.split()
	print words[2]









	