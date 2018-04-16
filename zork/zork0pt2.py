# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 14:16:10 2015
150316 - need to possibly put the IF tests which handle input into the class functions

@author: sharland
"""
import csv

class Home1:

#building starts at east and then goes in clockwise
#exterior locations

    #locpos = location where currently standing
    #dir1 to 4 = locations one can go

    def location(self,locpos,dir1,dir2,dir3,dir4):
        print("You are {0}".format(locpos))
        if dir4 == "":
            print("You may go {0},{1} or {2}".format(dir1,dir2,dir3))
        elif dir3 == "" and dir4 == "":
            print("You may go {0} or {1}".format(dir1,dir2))
        elif dir2 == "" and dir3 == "" and dir4 == "":
            print("You may go {0}".format(dir1))
        else:
            print("You may go {0},{1},{2} or {3}".format(dir1,dir2,dir3,dir4))

        direction = input(">")
        contAsking = True
        while contAsking == True:
            if direction == dir1:
                print("You went {0}".format(dir1))
                contAsking = False
                return dir1
            elif direction == dir2:
                print("You went {0}".format(dir2))
                contAsking = False
                return dir2
            elif direction == dir3:
                print("You went {0}".format(dir3))
                contAsking = False
                return dir3
            elif direction == dir4:
                print("You went {0}".format(dir4))
                contAsking = False
                return dir4
            else:
                print("Please enter {0},{1},{2} or {3}".format(dir1,dir2,dir3,dir4))
                direction = input(">")

    def openCSV(self,fileName): #opens the CSV file
        openFile = open(fileName+".csv",newline="") #gets the file input by user
        reader = csv.reader(openFile,delimiter=",") #creates a reader object with all data items
        global positions #need a global definition for positions - would there be a way of getting rid of it?
        positions = [] #empty list to append positions values

        for row in reader: #iterate over reader object to get rows
            positions.append(row) #add them back to the positions list
        return positions #return value of positions to be used elsewhere

if __name__ == '__main__': #used to run code only if file is run directly - not if imported
    pass

squareA1 = Home1()      #calls location object as a unique square name

whichFile = input("Which game would you like to play?: ") #need to add something which scans for csv files in that directory

squareA1.openCSV(whichFile)

locpos = positions[1][0] #gets the current position (stored first row of CSV)
#below four lines get the possible directions from the same row as locpos
dir1 = positions[1][1]
dir2 = positions[1][2]
dir3 = positions[1][3]
dir4 = positions[1][4]

contGame = True

while contGame == True:
    squareA1.location(locpos,dir1,dir2,dir3,dir4) #puts you into position

#now need a way to call location again with the new information
#the csv row storing the game position will probably need:
    #- the overall position name
    #- possible directions to go
    #- the new positions as a result of having gone that directions
    #- will need to write something which based on which direction has been chosen
    #- automatically adds four in order to get the new position
    #- now need to loop back through the csv rows in order to find the new position row
    #- now ask from there
    
