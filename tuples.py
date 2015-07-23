#Tuples are like lists
x = ('Glenn', 'Sally', 'Joseph')
print x[2]
y = (1, 9, 2)
print max(y)

y = (1, 9, 2)
for iter in y:
	print iter

#But Tuples are "immutable"
	#Unlike lists once you create a tuple, you cannot alter its contents - smilar to a string
	# a tale of two Sequences
	l = list()
	dir(l)
	

	t = tuple()
	dir(t)

#Tuples and assignments
(x,y) = (4, 'fred')
print y

(a,b) = (99, 98)
print a

#Tulpes and dictionaries
d = dict()
d['csev'] = 2
d['cwen'] = 4
for (k,v) in d.items():
	print k, v

tups = d.items()
print tups

#Tuples are compareable
q = (0,1,2) < (5,1,2)
print q

#Sorting lists of tuples

d = {'a':10, 'b':1, 'c':22}
t = d.items()
print t

t.sort()
print t

#Using sorted()
d = {'a':10, 'b':1, 'c':22}
d.items()
t = sorted(d.items())
print t

for k, v in sorted(d.items()):
	print k, v

#Sort by values instead of key
c = {'a':10, 'b':1, 'c':22}
tmp = list()
for k, v in c.items():
	tmp.append( (v,k) )

print tmp
tmp.sort(reverse=True)
print tmp

#Top ten most common words
fhand = open('romeo.txt')
counts = dict()
for line in fhand:
	words = line.split()
	for word in words:
		counts[word] = counts.get(word, 0) + 1

lst = list()
for key, val in counts.items():
	lst.append( (val, key) )

lst.sort(reverse=True)

for val, key in lst[:10] :
	print key, val


#Even shoter version
c = {'a':10, 'b':1, 'c':22}
print sorted ( [ (v,k) for k,v in c.items() ] )




