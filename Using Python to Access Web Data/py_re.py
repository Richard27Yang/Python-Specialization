
import re

filehandle=open('regex_sum_173908.txt','r')
value=0
num=0
for line in filehandle:
    line = line.rstrip()
    y=re.findall('([0-9]+)',line)
    if y!=[]:
        for number in y:
            num=num+1
            value=value+int(number)
            print number
print num
print value
