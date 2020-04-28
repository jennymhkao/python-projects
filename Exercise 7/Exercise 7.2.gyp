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
