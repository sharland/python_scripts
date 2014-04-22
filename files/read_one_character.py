#! /usr/local/bin/python3

f = open("/Users/sharland/Dropbox/Computing_department/Python/python_scripts/files/temp","r")
print("The first letter is:")
print(f.read(1))
print("The second letter is:")
print(f.read(1))
f.close()
