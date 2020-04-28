'''Change your socket program so that it counts the number of 
characters it has received and stops displaying any text after 
it has shown 3000 characters. The program should retrieve the 
entire document and count the total number of characters and 
display the count of the number of characters at the end of 
the document.
'''

import urllib.request, urllib.parse, urllib.error

try:
    fname = input('Enter URL: ')   
    fhand = urllib.request.urlopen((fname))     
except:
    print('URL does not exist', fname)
    exit()

count = 0
counts = dict()
for line in fhand:
    chars = line.decode().strip().split()
    for char in chars[:3000]:
        counts[char] = counts.get(char, 0) + 1
        count += 1
print(counts)
print('number of characters:', count)
    