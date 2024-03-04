# 10.2 Write a program to read through the mbox-short.txt and 
# figure out the distribution by hour of the day for each of
# the messages. You can pull the hour out from the 'From ' line by
# finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts,
# sorted by hour as shown below.

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
    
handle = open(name)

mail_count=dict()

for line in handle:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    else:
        words = line.split()
        for word in words:
            time=words[5]
            hour=time.split(":")
            key=hour[0]
            
        mail_count[key]=mail_count.get(key,0) + 1

#print(mail_count)

lst=sorted( [ (k,v) for k,v in mail_count.items() ] )

for key,value in lst:
    print(key,value)