try:
	hrs = raw_input("Enter hours:")
	h = float(hrs)
	pay = raw_input("Enter Rate:")
	payf = float(pay)
	
except:
		print"Error, plese enter numeric input"
		quit()

if h <= 40:
		rate = h * payf
		print rate
else:
		r = h * payf + (payf * 1.5 * (h - 40))
		print "You made",r

