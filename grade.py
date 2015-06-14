try:
	grade = raw_input("Enter grade:")
	gradef = float(grade)

except:
	print("Enter a grade that is a number and falls within the range between 0.0-1.0")
	quit()

if 0.9 <= gradef <= 1.0:
	print "A"
if 0.8 <= gradef < 0.9:
	print "B"
if 0.7 <= gradef < 0.8:
	print "C"
if 0.6 <= gradef < 0.7:
	print "D"
if 0.0 <= gradef < 0.6:
	print "F"
elif gradef > 1.0:
	print"The grade is too high."
elif gradef < 0:
	print "The grade is too low."