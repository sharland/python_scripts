#!f:
#filename: create_records.py using class/records

    
def create_file():
    currentFile = open("namesandages.txt","w")
    for i in range(1,3): # enters 2 blank names and ages
        print('enter forename ')
        forename = input()
        print('enter surname')
        surname = input()
        print('enter age')
        age = input()
        newline = forename + (" ") + surname+ " " + age
        newline += ("\n")#puts each string on a new line in file
        currentFile.write(newline)
    currentFile.close()
    return

def read_file():
    currentFile = open("namesandages.txt","r")
    for i in range(1,3): # reads 2 names and ages
        linefromfile = currentFile.readline()
        forename = ""
        count = 0
        while count < len(linefromfile) and linefromfile[count] != " ":
            forename = forename + linefromfile[count]
            count += 1
        print('forename = ',forename)  #need to store into records/arrays/list
    currentFile.close()       
    return
            

        
create_file()
read_file()
