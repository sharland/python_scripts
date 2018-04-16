#!f:
#filename: creating, reading and adding to a text file

    
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
        surname = ""
        count += 1
        while count < len(linefromfile) and linefromfile[count] != " ":
            surname = surname + linefromfile[count]
            count += 1
        age = ""
        count += 1
        while count < len(linefromfile) and linefromfile[count] != " ":
            age = age + linefromfile[count]
            count += 1
        print('forename =',forename, 'surname =',surname, 'age =',age) 
    currentFile.close()       
    return
            
def append_file():
    currentFile = open("namesandages.txt","a")#append mode
    for i in range(1,3): # enters 2 more names
        print('enter forename ')
        forename = input()
        print('enter surname')
        surname = input()
        print('enter age')
        age = input()
        newline = forename + (" ") + surname + " " + age
        newline += ("\n")#puts each string on a new line in file
        currentFile.write(newline)
    currentFile.close()
    return



        
create_file()
read_file()
append_file()
