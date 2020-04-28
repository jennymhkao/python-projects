'''Change the socket program socket1.py to prompt 
the user for the URL so it can read any web page. 
You can use split('/') to break the URL into its 
component parts so you can extract the host name 
for the socket connect call. Add error checking 
using try and except to handle the condition where 
the user enters an improperly formatted or non-existent URL.
import socket
'''

import socket

try:
    fname = input('Enter URL: ')    
    words = fname.split('/')
    host = words[2]
except:
    print('URL does not exist', fname)
    exit()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, 80))
request = (('GET '+fname+' HTTP/1.0\r\n\r\n').encode())
sock.send(request)

while True:
    data = sock.recv(512)
    if(len(data) < 1):
        break
    print(data.decode(), end='')
    
sock.close()
