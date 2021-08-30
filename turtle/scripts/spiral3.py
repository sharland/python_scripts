#! /usr/local/bin/python3

from turtle import *
import random

setup(500,500)
colormode(255)
speed(0)
hideturtle()


def drawShape(distance,angle,sides,r,g,b,redDirection,greenDirection,blueDirection):

	pencolor(r,g,b)
	
	for count in range(sides):
		forward(distance)
		left(angle)

	
def start():
	sides = int(input("Enter number of sides: "))
	no_shapes = int(input("Number of shapes: "))
	angle = 360/sides
	n = 0
	
	r = random.randint(0,255)
	g = random.randint(0,255)
	b = random.randint(0,255)

	redDirection = True
	greenDirection = True
	blueDirection = True
	
	for count in range(no_shapes):		
		distance = n
		drawShape(distance,angle,sides,r,g,b,redDirection,greenDirection,blueDirection)
		n += 1
		left(1)
		if redDirection == True:
			r += 1
		if r == 255:
			redDirection = False
			
		if redDirection == False:
			r -= 1
		if r == 0:
			redDirection = True
	
		if greenDirection == True:
			g += 1
		if g == 255:
			greenDirection = False
			
		if greenDirection == False:
			g -= 1
		if g == 0:
			greenDirection = True
		
		if blueDirection == True:
			b += 1
		if b == 255:
			blueDirection = False
			
		if blueDirection == False:
			b -= 1
		if b == 0:
			blueDirection = True
		
start()

done()


 
