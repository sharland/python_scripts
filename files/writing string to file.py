x = 3
y = " is the magic number"

f = open("/Users/sharland/Dropbox/Computing department/Python/python scripts/files/temp","w") #"w" means the old file will be overwritten
x = str(x)
f.write(x + y)
f.close()

f = open("/Users/sharland/Dropbox/Computing department/Python/python scripts/files/temp","r")
print(f.read())
f.close()

         
