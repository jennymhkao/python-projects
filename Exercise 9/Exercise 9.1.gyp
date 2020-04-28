fname = input('Enter file name: ')
try:    
    if len(fname) < 1 : fname = 'romeo.txt'
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

di = dict()
for line in fhand:
    line = line.rstrip()
    words = line.split()
    for w in words:
        di[w] = di.get(w)
print(di)

