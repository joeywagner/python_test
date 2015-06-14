hrs = raw_input("Enter hours:")

h = float(hrs)
pay = raw_input("Enter Rate:")
payf = float(pay)
h2 = h - 40

if h == 40:
	rate = h * payf
	print rate
if h < 40:
	r = h * payf
	print "You made",r
if h > 40:
	rate = (h2 * payf * 1.5) + 420.00
	print 'You made $', rate