#!f:
#filename: createnewfile.py
def create_file():
    currentFile = open("names.txt","w")#write mode
    for i in range(1,3): # enters 2 names
        print('enter forename ')
        forename = input()
        print('enter surname')
        surname = input()
        newline = forename + (" ") + surname
        newline += ("\n")#puts each string on a new line in file
        currentFile.write(newline)
    currentFile.close()
    return

create_file()
