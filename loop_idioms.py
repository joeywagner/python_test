print 'Before'
for thing in [9,41,12,3,74,15]:
	print thing
print 'After'

# finding the largest value
largest_so_far = -1
print 'Before', largest_so_far
for the_num in [9,41,12,3,74,15]:
	if the_num > largest_so_far:
		largest_so_far = the_num
	print largest_so_far, the_num

print 'after', largest_so_far

#Counting loop
zork = 0
print 'Before', zork
for thing in [9, 41, 12, 3, 74, 15]:
	zork = zork + 1
	print zork, thing
print 'After', zork

#Summing in a loop
zork = 0
print 'Before', zork
for thing in [9, 41, 12, 3, 74, 15]:
	zork = zork + thing
	print zork, thing
print 'After', zork


#finding the average in a loop
count = 0
sum = 0
print 'Before',count,sum
for value in [9, 41, 12, 3, 74, 15]:
	count = count + 1
	sum = sum + value
	print count, sum, value
print 'After', count, sum, sum/count


#Filtering in a loop
print 'Before'
for value in [9,41,12,3,74,15]:
	if value > 20:
		print 'Large number', value
print 'After'


#Search using a boolean Variable
found = False
print 'Before', found
for value in [9, 41, 12, 3, 74, 15]:
	if value == 3:
		found = True
	print found, value

print 'After', found