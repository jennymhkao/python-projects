fname = input('Enter file: ')
try:
    fhand = open(fname)
except: 
    print('File cannot be opened:', fname)
    exit()

count = 0
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From'): continue
    words = line.split()
    print(words[1])
    count = count + 1
    #print(count)

print("There were", count, "lines in the file with From as the first word")

