largest = None
smallest = None
while True:
	num = raw_input("Enter a number: ")
	if num == "done" : break
	print num

	try:
		num = int(num)
	except:
		print "Invalad input"
		continue
	if smallest is None:
		smallest = num
	elif num < smallest:
		smallest = num
	#print smallest

	if largest is None:
		largest = num
	elif num > largest:
		largest = num
	#print largest

print "Maximum", largest
print "Minimum", smallest