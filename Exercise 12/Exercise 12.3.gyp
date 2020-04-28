'''Use urllib to replicate the previous exercise of (1)
retrieving the document from a URL, (2) displaying up 
to 3000 characters, and (3) counting the overall number 
of characters in the document. Don't worry about the 
headers for this exercise, simply show the first 3000 
characters of the document contents.
'''

import urllib.request, urllib.parse, urllib.error
import ssl

#Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ') 
try:  
    fhand = urllib.request.urlopen(url, context=ctx)
except:
    print("URL doesn't exist")

counts = dict()
for line in fhand:
    words = line.split()
    if len(words) < 3000:
        for word in words:
            counts[word] = counts.get(word, 0) + 1
            print(counts)
            