fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

emailcount=dict()

fh = open(fname)
count = 0
for line in fh:
    line = line.rstrip()
    if not line.startswith('From ') : continue
    words = line.split()
    email = words[1]
    emailcount[email]=emailcount.get(email,0)+1
#print emailcount
num=0
emailget=''
for email, count in emailcount.items():
    if count > num : 
        num = count
        emailget = email 
print emailget, num
