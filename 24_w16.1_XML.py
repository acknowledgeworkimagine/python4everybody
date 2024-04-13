import xml.etree.ElementTree as ET

data1 = '''
<person>
    <name>Chuck</name>
    <phone type = "intl" >
    +1 734 303 4456
    </phone>
    <email hide = "yes" />
</person> '''

tree = ET.fromstring(data1)
print('----Exercise #1----')
print('Name:', tree.find('name').text) # .find gives us just one tag.
print('Attr:', tree.find('email').get('hide'))

data2 = '''
<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
        </user>
    </users>
</stuff>'''

stuff = ET.fromstring(data2)
lst = stuff.findall('users/user') # .findall return the list of all tags.
print('----Exercise #2----')
print('User count:', len(lst))

for item in lst:
    print('Name:', item.find('name').text)
    print('Id:', item.find('id').text) 
    print('Attribute:', item.get("x"))

