#! /usr/local/bin/python3

#note the early use of curly brackets at the start and end of the dictionary and colons to separate the key/value pairs

logins = {"john":"yellow","paul":"red","george":"blue","ringo":"green"}

#print all the keys

for item in logins:
    print(item)

#print all the values

for item in logins:
    print(logins[item])

#print both

for key, value in logins.items():
    print("The key is:", key, "and the value is:", value)
    
