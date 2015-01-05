#! /usr/local/bin/python3

from turtle import *
import random

setup(500,500,0,0)
speed(0)
colormode(255)
hideturtle()
tracer(0)
penup()
setpos(-200,200)
pendown()

## lists to store colour values
red = []
green = []
blue = []

for i in range (256):
	red.append(i)
	green.append(i)
	blue.append(i)

## set a starting rgb value
randomRed = random.randint(0,255)
randomGreen = random.randint(0,255)
randomBlue = random.randint(0,255)

## get a random direction for looping through the colour values
redChoice = random.randint(0,1)
if redChoice == 0:
	redDirection = False
else:
	redDirection = True
	
greenChoice = random.randint(0,1)
if greenChoice == 0:
	greenDirection = False
else:
	greenDirection = True
	
blueChoice = random.randint(0,1)
if blueChoice == 0:
	blueDirection = False
else:
	blueDirection = True


for i in range(200):
##	print("r",randomRed,"g",randomGreen,"b",randomBlue)
	pencolor(randomRed,randomGreen,randomBlue)
	right(90)
	random1 = random.randint(0,300)
	random2 = random.randint(0,300-random1)
	random3 = 400-(random1+random2)
	forward(random1)
	penup()
	forward(random2)
	pendown()
	forward(random3)
	left(90)
	penup()
	forward(1)
	pendown()
	left(90)
	
	
	if redDirection == True:
		randomRed += 1
		if randomRed == 255:
			redDirection = False
			
	if redDirection == False:
		randomRed -= 1
		if randomRed == 0:
			redDirection = True
	
	if greenDirection == True:
		randomGreen += 1
		if randomGreen == 255:
			greenDirection = False
			
	if greenDirection == False:
		randomGreen -= 1
		if randomGreen == 0:
			greenDirection = True
		
	if blueDirection == True:
		randomBlue += 1
		if randomBlue == 255:
			blueDirection = False
			
	if blueDirection == False:
		randomBlue -= 1
		if randomBlue == 0:
			blueDirection = True
	
	random1 = random.randint(0,300)
	random2 = random.randint(0,300-random1)
	random3 = 400-(random1+random2)
	forward(random1)
	penup()
	forward(random2)
	pendown()
	forward(random3)
	right(90)
	penup()
	forward(1)
	pendown()
	
	
done()