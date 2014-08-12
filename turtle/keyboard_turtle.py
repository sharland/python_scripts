#! /usr/local/bin/python3

from turtle import *

colormode(1.0)
delay(0)

def goUp():
    setheading(90)
    forward(50)

def goDown():
    setheading(270)
    forward(50)

def goLeft():
    setheading(180)
    forward(50)

def goRight():
    setheading(0)
    forward(50)

def saveImage():
    fileName = input("Enter file name: ")
    turtleImage = getscreen()
    turtleImage.getcanvas().postscript(file=fileName+".eps")
    print("File saved as ",fileName+".eps")

def paintCircles():
    dot(50,"red")


    
onkey(goUp,"w")
onkey(goDown,"s")
onkey(goLeft,"a")
onkey(goRight,"d")

onclick(paintCircles,1,False)

ondrag(goto)


listen()

done()
