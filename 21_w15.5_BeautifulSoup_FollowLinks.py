# https://pypi.org/project/beautifulsoup4/

import urllib.request, urllib.parse, urllib.error
from  bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Address for the exercise: http://py4e-data.dr-chuck.net/known_by_Fikret.html
url = input('Enter URL: ')
#use for the exercise: 4
count = input('Enter count: ') 
#use for the exercise: 3
position = input('Enter position: ')

i=0 #count
while i<=int(count):
    n=0 #position
    print('Retrieving:', url)
    html = urllib.request.urlopen(url, context = ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
        #print(i)
    for tag in tags:
        if n>= int(position):
            break
        url = tag.get('href', None)
        #print(url)
        n = n+1
    i = i+1