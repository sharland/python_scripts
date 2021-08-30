#!f:
#filename: appendtofile.py
def append_file():
    currentFile = open("names.txt","a")#append mode
    for i in range(1,3): # enters 2 more names
        print('enter forename ')
        forename = input()
        print('enter surname')
        surname = input()
        newline = forename + (" ") + surname
        newline += ("\n")#puts each string on a new line in file
        currentFile.write(newline)
    currentFile.close()
    return

append_file()
