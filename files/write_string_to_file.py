#! /usr/local/bin/python3

x = 3
y = " is the magic number"

f = open("/Users/sharland/dropbox/computing_department/python/python_scripts/files/temp","w") #"w" means the old file will be overwritten
x = str(x)					#casts x which was an integer from line 3 as a string so that it can be written to the file
f.write(x + y)				#writes the values assigned to x and y
f.close()

f = open("/Users/sharland/Dropbox/computing_department/python/python_scripts/files/temp","r")
print(f.read())
f.close()

         
