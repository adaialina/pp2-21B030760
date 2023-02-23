import re
str = input()
a = re.findall("[A-Z]+[a-z]+$", str)
if a:
    print('found')
else:
    print('not found')