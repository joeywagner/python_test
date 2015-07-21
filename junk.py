name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts = dict()
for line in handle:
    words = line.split()
    if len(words) < 2 : continue
    if words[0] != "From" : continue
    email = words[1]
    print email
    counts[email] = counts.get(email,0) + 1
bigcount = None
bigname = None
for name,count in counts.items():
    if bigname is None or count > bigcount:
        bigname = name
        bigcount = count
print bigname, bigcount