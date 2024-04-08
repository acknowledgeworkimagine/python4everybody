import urllib.request, urllib.parse, urllib.error
import ssl
import xml.etree.ElementTree as ET

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Address  for the exercise: http://py4e-data.dr-chuck.net/comments_42.xml
url = input('Enter location: ')

print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()
print('Retrieved', len(data), 'characters')
#print(data.decode())

xml = ET.fromstring(data)
lst = xml.findall('.//comment') # .findall return the list of all tags.
print('Count:', len(lst))
sum = 0
for item in lst:
    value = int(item.find('count').text)
#print(value)
    sum = sum + value
print('Sum:', sum)