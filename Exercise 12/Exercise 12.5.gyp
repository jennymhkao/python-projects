'''Exercise  12.5: (Advanced) Change the socket program 
so that it only shows data after the headers and a blank 
line have been received. Remember that recv is receiving 
characters (newlines and all), not lines.
'''

import socket
import re

try:
    fname = input('Enter URL: ')    
    words = fname.split('/')
    host = words[2]
except:
    print('URL does not exist', fname)
    exit()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, 80))
request = ('GET '+fname+' HTTP/1.0\r\n\r\n').encode()
sock.send(request)

data = sock.recv(512)
message = data.decode()

# Find the end of header & add four to exclude:'\r\n\r\n'
header_end_pos = message.find('\r\n\r\n') + 4

print(message[header_end_pos:])
while True:
    # Header in the first data only
    data = sock.recv(512) 
    if not data:
        break
    print(data.decode())
    
sock.close()