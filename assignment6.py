text = '"X-DSPAM-Confidence:    0.8475";'
space = text.find(':')
#print space

number = text.find('"', space)
#print number

integer = text[space+1:number]
intergers = integer.strip()

#print intergers
floatint=float(intergers)
print floatint