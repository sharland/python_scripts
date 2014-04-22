#! /usr/local/bin/python3

#open a file and assign that file to a variable
f = open("/Users/sharland/Dropbox/computing_department/python/python_scripts/files/temp","r")

#print the contents of the file (through reading it)
print(f.read())

#close the file (should always do!)
f.close()

         
