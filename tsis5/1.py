import re 
str = str(input())
aAndBs = re.search("ab*", str)

if aAndBs:
    print("Yes")
else:
    print("No")