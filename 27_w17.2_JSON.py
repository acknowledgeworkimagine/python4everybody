#https://www.json.org/json-en.html
import json

data = '''[
    {
        "id" : "001",
        "x" : "2",
        "name" : "Chuck"
    },
    {
        "id" : "009",
        "x" : "7",
        "name" : "Elias"
    }
]'''

info = json.loads(data)
print('User count', len(info))
print("\n")
for item in info:
    print('Name: ', item['name'])
    print('Id: ', item['id'])
    print('Attribute: ', item['id'])
    print("\n")
