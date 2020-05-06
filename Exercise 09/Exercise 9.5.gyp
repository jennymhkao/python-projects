'''This program records the domain name 
(instead of the address) where the message 
was sent from instead of who the mail came 
from (i.e., the whole email address). At 
the end of the program, print out the contents 
of your dictionary.
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
        email = words[1]
        email = email.split('@')
        di[email[1]] = di.get(email[1], 0) + 1
print(di)
