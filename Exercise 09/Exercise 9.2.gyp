'''Write a program that categorizes each mail 
message by which day of the week the commit was 
done. To do this look for lines that start with 
"From", then look for the third word and keep a 
running count of each of the days of the week. 
At the end of the program print out the contents 
of your dictionary (order does not matter).

Sample Line: 

From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

Sample Execution:

Enter a file name: mbox-short.txt
{'Fri': 20, 'Thu': 6, 'Sat': 1}'''

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
    