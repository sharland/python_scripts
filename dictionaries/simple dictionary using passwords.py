#! /usr/bin/env python3

#note the early use of curly brackets at the start and end of the dictionary and colons to separate the key/value pairs

logins = {"john":"yellow","paul":"red","george":"blue","ringo":"green"}
print("george's password is ",logins["george"])

#change george's password to a new value
logins["george"] = "purple"
print("Changing George's password to purple")
print(logins)
