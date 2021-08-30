#! /usr/local/bin/python3

from turtle import *

def moveForward():
	forward(10)
	stamp()
	
def moveBackward():
	backward(10)
	dot()
	
def turnLeft():
	left(45)
	
def turnRight():
	right(45)

listen()

onkey(moveForward,"Up")
onkey(moveBackward,"Down")
onkey(turnLeft,"Left")
onkey(turnRight,"Right")


done()