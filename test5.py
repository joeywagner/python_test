largest = None
smallest = None
while True:
	num = raw_input("Enter a number: ")
	if num == "done" : break
	print num

	try:
		num = float(inp)
	except:
		print "Invalad input"

	if smallest is None:
		smallest = num
	elif num < smallest:
		smallest = num
	print smallest, num

	if largest is None:
		largest = num
	elif num > largest:
		largest = num
	print largest, num

print "Maximum", largest
print "Minimum", smallest