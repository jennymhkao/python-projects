import sqlite3

'''
    This program will read the mailbox data (mbox.txt) and count the number of email
    messages per organization (i.e. domain name of the email address) using a database with
    the following schema to maintain the counts.
'''

conn = sqlite3.connect('emaildb.sqlite') # creates a connection object that represents the db
cur = conn.cursor() # creates a cursor object

cur.execute('''DROP TABLE IF EXISTS Counts''')
cur.execute('''CREATE TABLE Counts (email TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    # doesn't retrieve data, rather looking at SQL and verify table name is correct
    cur.execute('SELECT count FROM Counts WHERE email = ? ', (email, )) 
    row = cur.fetchone() # grab the information from db into row
    if row is None:
        cur.execute('''INSERT INTO Counts (email, count) VALUES (?, 1)''', (email, ))
    else:
        # if row exists, then update the number
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?', (email, ))
    conn.commit()

sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr): 
    print(str(row[0]), row[1]) # row [0] is email string, row[1] is count

cur.close()