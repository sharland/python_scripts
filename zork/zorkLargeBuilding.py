# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 14:16:10 2015
150316 - need to possibly put the IF tests which handle input into the class functions

@author: sharland
"""

class Home1:
    
#building starts at east and then goes in clockwise
#exterior locations

    #create 'switchboard' to handle which location is active
    direction = "up"
    
    def buildingExtE(self):
        print("You are at the E side of the building")
        print("You may go S, N, or E")
        direction = input(">")
        if direction == "N":
            self.exteriorN()
        elif direction == "W":
            self.exteriorNW()
        elif direction == "E":
            self.exteriorNE()
        else:
            print("please enter N, E or W")
            self.buildingExtN()
        
    def buildingExtSE(self):        
        print("You are at the SE side of the building")
        print("You may go W, N or SE")
        direction = input(">")
        if direction == "N":
            self.exteriorN()
        elif direction == "W":
            self.exteriorNW()
        elif direction == "E":
            self.exteriorNE()
        else:
            print("please enter N, E or W")
            self.buildingExtN()
        
    def buildingExtS(self):        
        print("You are at the S side of the building")
        print("You may go W, E or S")
        direction = input(">")
        if direction == "N":
            self.exteriorN()
        elif direction == "W":
            self.exteriorNW()
        elif direction == "E":
            self.exteriorNE()
        else:
            print("please enter N, E or W")
            self.buildingExtN()
        
        
    def buildingExtSW(self):        
        print("You are at the SW side of the building")
        print("You may go E, N or SW")   
        direction = input(">")
        if direction == "N":
            self.exteriorN()
        elif direction == "W":
            self.exteriorNW()
        elif direction == "E":
            self.exteriorNE()
        else:
            print("please enter N, E or W")
            self.buildingExtN()
        
    def buildingExtW(self):        
        print("You are at the W side of the building")
        print("You may go N, S or W")
        direction = input(">")
        if direction == "N":
            self.exteriorN()
        elif direction == "W":
            self.exteriorNW()
        elif direction == "E":
            self.exteriorNE()
        else:
            print("please enter N, E or W")
            self.buildingExtN()
        
    def buildingExtNW(self):            
        print("You are at the NW side of the building")
        print("You may go S, E or Nw") 
        direction = input(">")
        if direction == "N":
            self.exteriorN()
        elif direction == "W":
            self.exteriorNW()
        elif direction == "E":
            self.exteriorNE()
        else:
            print("please enter N, E or W")
            self.buildingExtN()
        
    def buildingExtN(self):        
        print("You are at the N side of the building")
        print("You may go W, E or N")
        direction = input(">")
        if direction == "N":
            self.exteriorN()
        elif direction == "W":
            self.exteriorNW()
        elif direction == "E":
            self.exteriorNE()
        else:
            print("please enter N, E or W")
            self.buildingExtN()
        
    def buildingExtNE(self):        
        print("You are at the NE side of the building")
        print("You may go W, S or NE")
        direction = input(">")
        if direction == "N":
            self.exteriorN()
        elif direction == "W":
            self.exteriorNW()
        elif direction == "E":
            self.exteriorNE()
        else:
            print("please enter N, E or W")
            self.buildingExtN()
  

#exterior of game square
    def exteriorE(self):
        print("You are looking E")
        print("You may go S, N, or E")
        direction = input(">")
        if direction == "N":
            self.exteriorN()
        elif direction == "W":
            self.exteriorNW()
        elif direction == "E":
            self.exteriorNE()
        else:
            print("please enter N, E or W")
            self.buildingExtN()
        
    def exteriorSE(self):
        print("You are looking SE")
        print("You may go S, N, or E")
        direction = input(">")
        if direction == "N":
            self.exteriorN()
        elif direction == "W":
            self.exteriorNW()
        elif direction == "E":
            self.exteriorNE()
        else:
            print("please enter N, E or W")
            self.buildingExtN()
        
    def exteriorS(self):
        print("You are looking S")
        print("You may go S, N, or E")
        direction = input(">")
        if direction == "N":
            self.exteriorN()
        elif direction == "W":
            self.exteriorNW()
        elif direction == "E":
            self.exteriorNE()
        else:
            print("please enter N, E or W")
            self.buildingExtN()
        
    def exteriorSW(self):
        print("You are looking SW")
        print("You may go S, N, or E")
        direction = input(">")
        if direction == "N":
            self.exteriorN()
        elif direction == "W":
            self.exteriorNW()
        elif direction == "E":
            self.exteriorNE()
        else:
            print("please enter N, E or W")
            self.buildingExtN()
        
    def exteriorW(self):
        print("You are looking W")
        print("You may go S, N, or E")
        direction = input(">")
        if direction == "N":
            self.exteriorN()
        elif direction == "W":
            self.exteriorNW()
        elif direction == "E":
            self.exteriorNE()
        else:
            print("please enter N, E or W")
            self.buildingExtN()
        
    def exteriorNW(self):
        print("You are looking NW")
        print("You may go S, N, or E")
        direction = input(">")
        if direction == "N":
            self.exteriorN()
        elif direction == "W":
            self.exteriorNW()
        elif direction == "E":
            self.exteriorNE()
        else:
            print("please enter N, E or W")
            self.buildingExtN()
        
    def exteriorN(self):
        print("You are looking N")
        print("You may go S, N, or E")
        direction = input(">")
        if direction == "N":
            self.exteriorN()
        elif direction == "W":
            self.exteriorNW()
        elif direction == "E":
            self.exteriorNE()
        else:
            print("please enter N, E or W")
            self.buildingExtN()
        
    def exteriorNE(self):
        print("You are looking NE")
        print("You may go S, N, or E")
        direction = input(">")
        if direction == "N":
            self.exteriorN()
        elif direction == "W":
            self.exteriorNW()
        elif direction == "E":
            self.exteriorNE()
        else:
            print("please enter N, E or W")
            self.buildingExtN()
        
    def buildingRoom1(self):
        print("You are inside the building in a room")
        direction = input(">")
        if direction == "N":
            self.exteriorN()
        elif direction == "W":
            self.exteriorNW()
        elif direction == "E":
            self.exteriorNE()
        else:
            print("please enter N, E or W")
            self.buildingExtN()
        

    def building(self):
        #starting point for game square
        #provides general description of environment once you arrive
        #will need to figure out how to fetch departure vector from previous square
        #and then use that to figure out which exterior point individual arrives at
        #and then execute that function
        print("Welcome to the Building")
        print("you may move E, N, S, W, NE, NW, SE and SW")        
        

if __name__ == '__main__': #used to run code only if file is run directly - not if imported
    pass


squareA1 = Home1()
squareA1.building() #intro text
squareA1.buildingExtN() #puts you into position


    
