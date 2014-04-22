#! /usr/local/bin/python3

import re
url = input("Enter a website address: ")

if re.search("^http://",url):
    print("It begins with http:// - likely a web address")
else:
    print("No - doesn't begin with http://")
if re.search("[a-z]",url):
    print("it contains characters - success")
else:
    print("There are no characters in this string")
if re.search("\.",url):
    print("it contains full stops")
else:
    print("there are no full stops in this string")
    
