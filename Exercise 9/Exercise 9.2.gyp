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
        words = line.split()
        if len(words) > 2:
            #print(words)
            di[words[2]] = di.get(words[2], 0) + 1
print(di)
    