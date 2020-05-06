'''Write a program to prompt for a file name (mbox-short.txt), 
and then read through the file and look for lines of the form:

X-DSPAM-Confidence: 0.8475

When you encounter a line that starts with "X-DSPAM-Confidence:" 
pull apart the line to extract the floating-point number on the 
line. Count these lines and then compute the total of the spam 
confidence values from these lines. When you reach the end of 
the file, print out the average spam confidence.
'''

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except: 
    print('File cannot be opened:', fname)
    exit()
avg = 0
count = 0
for line in fhand:
    if not line.startswith('X-DSPAM-Confidence:')   :  continue
    #print(line)
    n = line.find(':')
    #print(n)
    y = line[n+2:]
    print(y)
    x = float(y)
    #print(x)
    count = count + 1
    #print(count)
    avg = (avg + x)
    #print(avg)
    

print("Average spam confidence:", avg / count)
