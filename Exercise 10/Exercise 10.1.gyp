'''Revise a previous program as follows: 
Read and parse the "From" lines and pull 
out the addresses from the line. Count 
the number of messages from each person 
using a dictionary.

After all the data has been read, print the 
person with the most commits by creating a 
list of (count, email) tuples from the dictionary. Then sort the list in reverse order and print out the person who has the most commits.
'''

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