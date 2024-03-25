import re

name = input("Enter file:")
if len(name) < 1:
    name = "regex_sum_1983829.txt"
    
handle = open(name)
sum = 0
for line in handle:
    line = line.rstrip()
    integers = re.findall('[0-9]+',line)
    for number in integers:
        sum = int(number) + sum
    
print('Sum:', sum)