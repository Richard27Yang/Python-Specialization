
#assignment 10.2 python data structure

fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

hourcount=dict()

fh = open(fname)
count = 0
for line in fh:
    line = line.rstrip()
    if not line.startswith('From ') : continue
    words = line.split()
    time = words[5].split(':')
    hour = time[0]
    hourcount[hour]=hourcount.get(hour,0)+1
#print emailcount
num=0
hourget=''
#for hour, count in hourcount.items():
tups = hourcount.items()
tups.sort()     
for hour, count in tups:
    print hour, count
