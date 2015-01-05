#! /usr/local/bin/python3

from turtle import *

title("Enter window title")
setup(500,500,0,0)
speed(0)
colormode(255)

def saveImage():
    hide()
    fileName = input("Enter file name: ")
    turtleImage = getscreen()
    turtleImage.getcanvas().postscript(file=fileName+".eps")
    print("File saved as ",fileName+".eps")

#All turtle code below here



#Don't put anything after here
onkey(saveImage,"s")
listen()
done()
