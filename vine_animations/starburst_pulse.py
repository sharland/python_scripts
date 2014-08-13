#! /usr/local/bin/python3

from turtle import *
from PIL import Image
import random
import os
import glob

title("Vine Video")
setup(480, 480, 0, 0)
delay(0)
hideturtle()

colormode(255)

def saveImage(fileName):
    turtleImage = getscreen()
    turtleImage.getcanvas().postscript(file=fileName+".eps")
    print("File saved as ",fileName+".eps")

def tiff2jpg(): ### Convert .tiff files to .jpg - function from @trevorappleton
 
    openFiles = glob.glob('*.eps')
    for files in openFiles:
 
        inFile = Image.open(files)
        fileName = os.path.splitext(files)[0] # gets filename
        outFile = fileName + ".jpg"
        inFile.save(outFile)
 
    return()

frames = [50,98,141,178,208,228,239]
filenames = ["frame1","frame2","frame3","frame4","frame5","frame6","frame7"]


for i in range(7):
    for j in range(150):
        randomRed = random.randint(1,254)
        randomGreen = random.randint(1,254)
        randomBlue = random.randint(1,254)

        randomLength = random.randint(0,frames[i])
        randomTurn = random.randint(-95,95)
        
        pencolor(randomRed,randomGreen,randomBlue)
        forward(randomLength)
        right(randomTurn)
        goto(0,0)
    saveImage(filenames[i])
    clear()

write("done - close turtle window now")

print("beginning conversion from .eps to .jpg")

tiff2jpg()

print("conversion eps to jpg done")

done()
        
        
        
    
    
    



