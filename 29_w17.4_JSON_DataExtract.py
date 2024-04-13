
# Notes on a url: https://py4e-data.dr-chuck.net/opengeo?q=Ann+Arbor%2C+MI
# ? means it is a query
# "q = " it read as, q equals query parameter
# + is the space 
# %2C is a URL encoded comma

import urllib.request, urllib.parse

#https://www.json.org/json-en.html

import json, ssl
#Address  for the exercise: https://py4e-data.dr-chuck.net/comments_42.json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
# url = "https://py4e-data.dr-chuck.net/comments_42.json"

print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()
print('Retrieved', len(data), 'characters')
    
try:
    js = json.loads(data)
except:
    js = None

# print(json.dumps(js, indent=4))

counter = 0
count=len(js['comments']) # https://py4e-data.dr-chuck.net/comments_42.json
print('Count:',count)

sum = 0
for i in range(count): # https://www.w3schools.com/python/ref_func_range.asp
    value = js['comments'][i]["count"]
    sum = value + sum
    
print('Sum:', sum)






