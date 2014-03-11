#! /usr/bin/python3.3

f = open("/Users/sharland/Dropbox/Computing_department/Python/python_scripts/files/temp","w")
for n in range(1,11):
    m = "This is test number " + str(n) + "\n"
    f.write(m)

f.close()
f = open("/Users/sharland/Dropbox/Computing department/Python/python scripts/files/temp","r")
print(f.read())
f.close()
