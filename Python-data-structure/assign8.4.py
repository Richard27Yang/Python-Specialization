fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    listline=line.split()
   # print line.rstrip()
   # print listline
    for word in listline:
        if word in lst: continue
#        print word
        lst.append(word)
#        print lst
lst.sort()
print lst
