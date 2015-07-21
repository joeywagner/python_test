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








