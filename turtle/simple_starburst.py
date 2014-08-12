#! /usr/local/bin/python3

from turtle import *
import random

title("Starburst")
setup(500, 500, 0, 0)

colormode(255)
delay(0)

randomRed = random.randint(1,254)
randomGreen = random.randint(1,254)
randomBlue = random.randint(1,254)

bgcolor(randomRed,randomGreen,randomBlue)

def saveImage():
    hide()
    fileName = input("Enter file name: ")
    turtleImage = getscreen()
    turtleImage.getcanvas().postscript(file=fileName+".eps")
    print("File saved as ",fileName+".eps")

for x in range (1,150):
	randomValue = random.randint(-95,200)
	randomRed = random.randint(1,254)
	randomGreen = random.randint(1,254)
	randomBlue = random.randint(1,254)
	pencolor(randomRed,randomGreen,randomBlue)
	forward(randomValue)
	right(randomValue)
	goto(0,0)

onkey(saveImage,"s")

listen()

done()
