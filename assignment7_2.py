# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
count = 0
num = 0
#newfloat = num + num
for line in fh:

    if not line.startswith("X-DSPAM-Confidence:") : continue

    line = line.rstrip()

    pos = line.find(':')
    
    num = num + float(line[pos+1:])
    #string = str(pos)
    #print num
    
    count = count + 1
   
    #total = num + num
    #print total
   

print "Average spam confidence:", num / count


