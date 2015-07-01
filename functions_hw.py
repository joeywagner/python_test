def computepay(h,r):
	
	if h <= 40:
		p = r * h
	else:
		p = r * 40 + (r * 1.5 * (h - 40))
		
	return p


try:
	inp = raw_input("Enter hours:")
	hours = float(inp)
	inp= raw_input("Enter Rate:")
	rate = float(inp)
	
except:
		print"Error, plese enter numeric input"
		quit()


pay = computepay(hours, rate)
print 'Your pay is:', pay