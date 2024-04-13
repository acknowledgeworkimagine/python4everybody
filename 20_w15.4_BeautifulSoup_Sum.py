# https://pypi.org/project/beautifulsoup4/

import urllib.request, urllib.parse, urllib.error
from  bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context = ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Address  for the exercise: https://py4e-data.dr-chuck.net/comments_42.html
# Retrieve all of the anchor tags
tags = soup('span')
sum = 0
count = 0
for tag in tags:
   # Look at the parts of a tag
   #print ('TAG:',tag)
   #print ('URL:',tag.get('href', None))
   number = tag.contents[0]
   count = count + 1
   sum = int(number) + sum
   #print ('Attrs:',tag.attrs)

print("Count ", count)
print("Sum", sum)


