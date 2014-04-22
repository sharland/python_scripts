#! /usr/local/bin/python3

#the following opens a file and writes some content to it
f = open("/Users/sharland/Dropbox/computing_department/python/python_scripts/files/temp","w")
for n in range(1,11):
    m = "This is a test number " + str(n) + "\n"						#adds in n as a string and then creates a new line using \n
    f.write(m)
f.close()

#the following simply opens the file and reads it in order to check that the above has been done correctly
f = open("/Users/sharland/Dropbox/computing_department/python/python_scripts/files/temp","r")
print(f.read())
f.close()
