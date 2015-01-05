#! /usr/local/bin/python3

from turtle import *

setup(1600,900,0,0)
speed(0)
colormode(255)
hideturtle()
penup()
setpos(266,-150)
pendown()

distance = 1

r = 0
g = 0
b = 0

redDirection = True
greenDirection = True
blueDirection = True

for i in range (2000):
	pencolor(r,g,b)
##	print("r",r,"g",g,"b",b)
	right(91)
	forward(distance)
	distance += 2
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


done()
