#! /usr/local/bin/python3

from turtle import *
from PIL import Image #imports image class
import random
import os, sys


title("Vine Video")
setup(700, 700, 0, 0)
speed(0)
hideturtle()
colormode(255)

def saveImage(fileName):
    turtleImage = getscreen()
    turtleImage.getcanvas().postscript(file=fileName+".eps")
    print("File saved as ",fileName+".eps")

frames = [0,73,142,206,260,303,333,348,348,333,303,260,206,142,73]
fileValue = 0

while fileValue < 181:
	
    for i in range(len(frames)): #create a set of frames based on length of list
        for j in range(180):
            randomRed = random.randint(1,254)
            randomGreen = random.randint(1,254)
            randomBlue = random.randint(1,254)

            randomTurn = random.randint(-95,95)
            randomLength = random.randint(0,frames[i])
            pencolor(randomRed,randomGreen,randomBlue)
            forward(randomLength)
            right(randomTurn)
            goto(0,0)
    
            
        filevalueString = str(fileValue)
        saveImage("frame"+filevalueString)
        
        inFile = Image.open("frame"+filevalueString+".eps")
        outFile = "frame"+filevalueString+".jpg"
        inFile.save(outFile)
        
        fileValue = int(fileValue)+1
    
        print("File converted to jpg")   
        clear()

write("done - close turtle window now")


done()
