'''Write a program to read through a mail log, 
build a histogram using a dictionary to count 
how many messages have come from each email 
address, and print the dictionary.

Then, add code to the above program to figure 
out who has the most messages in the file.

After all the data has been read and the dictionary 
has been created, look through the dictionary using 
a maximum loop (see Section [maximumloop]) to find 
who has the most messages and print how many messages 
the person has.
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