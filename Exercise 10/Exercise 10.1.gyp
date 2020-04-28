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
        address = words[1]
        di[address] = di.get(address, 0) + 1 
#print(di)

themost = list()
largest = -1
theemail = None
for k, v in di.items():
    #print(k, v)
    newt = (v, k)
    themost.append(newt)
#print('Flipped', themost)

themost = sorted(themost, reverse=True)
#print('Sorted', themost[:1])

for v, k in themost[:1]:
    print(k,v)