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
        if len(words) > 1:
            #idiom: retrieve/create/update counter
            di[words[1]] = di.get(words[1], 0) + 1

#print(di)

#find the most common email address used
largest = -1
theemail = None
for k,v in di.items():
    #print(k,v)
    if v > largest:
        largest = v
        theemail = k #capture/remember the key that was the largest
    
print('Done', theemail, largest)