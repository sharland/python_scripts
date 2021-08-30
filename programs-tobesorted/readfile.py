#!f:
#filename: readfile.py
def read_file():
    currentFile = open("names.txt","r")
    for i in range(1,3): # reads 2 names 
      # currentFile = open("names.txt","r")
        fullname = currentFile.readline()
        print(fullname)
    currentFile.close()
    return

read_file()
