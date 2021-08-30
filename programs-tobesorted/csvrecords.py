#!f:
#filename: creating, reading and adding to a text file

    
def create_file():

    currentFile = open("namesandages.csv","w")
    close = "n"
    while close == "n":

        print('enter forename ')
        forename = input()
        print('enter surname')
        surname = input()
        print('enter age')
        age = input()
        newline = forename + (",") + surname+ "," + age
        newline += ("\n")#puts each string on a new line in file
        currentFile.write(newline)
        closeFile = input("Do you want to close? (y/n): ")
        print(closeFile)
        if closeFile == "y":
            close = "y"

    currentFile.close()
    return

def read_file():
    currentFile = open("namesandages.csv","r")
    for i in range(1,5): # reads 4 names and ages
        linefromfile = currentFile.readline()
        forename = ""
        count = 0
        while count < len(linefromfile) and linefromfile[count] != ",":
            forename = forename + linefromfile[count]
            count += 1
        surname = ""
        count += 1
        while count < len(linefromfile) and linefromfile[count] != ",":
            surname = surname + linefromfile[count]
            count += 1
        age = ""
        count += 1
        while count < len(linefromfile) and linefromfile[count] != ",":
            age = age + linefromfile[count]
            count += 1
        print('forename =',forename, 'surname =',surname, 'age =',age) 
    currentFile.close()       
    return
            
def append_file():
 
    currentFile = open("namesandages.csv","a")#append mode
    close = "n"
    while close == "n":

        print('enter forename ')
        forename = input()
        print('enter surname')
        surname = input()
        print('enter age')
        age = input()
        newline = forename + (",") + surname + "," + age
        newline += ("\n")#puts each string on a new line in file
        currentFile.write(newline)
        closeFile = input("Do you want to close? (y/n): ")
        if closeFile == "y":
            close = "y"
    currentFile.close()
    return



        
create_file()
append_file()
read_file()


#---------------------------------------------------------------------------------
# File: csvreadfile.py

import csv

reader = csv.reader(open("namesandages.csv"))

for forename,surname,age in reader:
    print (forename,surname,age)

