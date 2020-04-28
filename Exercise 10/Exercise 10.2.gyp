fname = input('Enter file name: ')
try:    
    if len(fname) < 1 : fname = 'mbox-short.txt'
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

di = dict()

for line in fhand:
    if line.startswith('From'):
        words = line.rstrip()
        hour = words.split()
        if len(hour) > 2:
            #print(hour)
            counts = hour[5].split(':')
            #print(counts)
            new = counts[0]
            di[new] = di.get(new, 0) + 1
#print(di)

sort = list()
for k, v in di.items():
    print(k, v)
