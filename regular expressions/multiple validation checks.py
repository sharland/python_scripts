import re

string = "Now for something completely different"

if re.search("^N",string):
    print("Test 1 - Success!")      #will pass, it starts with "N"
if re.search("^for",string):
    print("Test 2 - Success!")      #will fail, it doesn't start with for
if re.search("\w$",string):
    print("Test 3 - Success!")      #will pass, it ends with a number or letter
if re.search("^.=t$",string):
    print("Test 4 - Succes!")       #will pass, it starts with a number of characters (^.+) and ends with a "t" (t$)
    
