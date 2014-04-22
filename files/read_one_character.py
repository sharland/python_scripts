#! /usr/local/bin/python3

f = open("/Users/sharland/Dropbox/Computing_department/Python/python_scripts/files/temp","r")
print("The first letter is:")
print(f.read(1))						#reads the first character
print("The second letter is:")
print(f.read(1))						#even though this still has 1 as an argument it will read the next character after character read in line 5
print("The third letter is:")
print(f.read(2))						#reads the next two characters
f.close()
