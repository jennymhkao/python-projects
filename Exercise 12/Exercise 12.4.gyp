'''Change the urllinks.py program to extract and 
count paragraph (p) tags from the retrieved HTML 
document and display the count of the paragraphs 
as the output of your program. Do not display the 
paragraph text, only count them. Test your program 
on several small web pages as well as some larger 
web pages.
'''

# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file


import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Initialize variables
count = 0

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()

# html.parser is the HTML parser included in the standard Python 3 library.
# information on other HTML parsers is here:
# http://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-a-parser
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the p tags
tags = soup('p')
for tag in tags:
    # Count paragraphs
    count += 1
print(count)