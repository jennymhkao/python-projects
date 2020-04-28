import urllib.request, urllib.parse, urllib.error
import ssl
from twurl import augment

# https://apps.twitter.com/
# Create App and get the four strings, put them in hidden.py

TWITTER_URL = 'https://api.twitter.com/1.1/statuses/user_timeline.json'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    print('')
    acct = input('Enter Twitter Account:')
    if (len(acct) < 1): break
    url = twurl.augment(TWITTER_URL,
                        {'screen_name': acct, 'count': '2'})
    print('Retrieving', url)
    
    # open the URL
    connection = urllib.request.urlopen(url, context=ctx)
    # read the data received and print first 250 words
    data = connection.read().decode()
    print(data[:250])
    
    # ask dictionary to get headers
    print ('===============================')
    headers = dict(connection.getheaders())
    # print headers
    print('Remaining', headers['x-rate-limit-remaining'])
