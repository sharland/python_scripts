#!f:
#filename: createfile.py using class/records
class person():
    def _init_(self):
        self.Forename = "-"
        self.Surname = "-"
        self.Age = 0
    
def create_file():
    currentFile = open("namesandages.txt","w")
    for i in range(1,3): # enters 2 names 
        print('enter forename ')
        forename = input()
        print('enter surname')
        surname = input()
        print('enter age')
        age = int(input())
        newline = self.forename + (" ") + self.surname + (" ") + str(self.age)
        newline += ("\n")#puts each string on a new line in file
        currentFile.write(newline)
    currentFile.close()
    return

create_file()
