#! /usr/local/bin/python3

f = open("/Users/sharland/Dropbox/Computing department/Python/python scripts/files/temp","r")
print(f.readline())
print("That was the first line")
print("")
f.seek(0)									#this returns the read point back to the first line
print(f.readline())
print("That was the first line again")
f.close()
