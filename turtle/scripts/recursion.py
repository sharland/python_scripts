#! /usr/local/bin/python3

from turtle import *
import random


title("Filling shapes")
setup(500, 500, 0, 0)
colormode(255)
speed(0)


#establish size of of circle and start position in order to position circle in middle of screen
#works on the basis that turtle always heads to right - I suppose I could make it certain with a setheading()
drawLength = [256,128,64,32,16,8,4,2,1]
drawItems = len(drawLength)
startPosition = drawLength[0]/2
penup()
setpos(-startPosition,startPosition)
pendown()

r = random.randint(1,255)
g = random.randint(1,255)
b = random.randint(1,255)
bgcolor(r,g,b)
r = random.randint(1,255)
g = random.randint(1,255)
b = random.randint(1,255)
pencolor(r,g,b)
r = random.randint(1,255)
g = random.randint(1,255)
b = random.randint(1,255)
fillcolor(r,g,b)

position = 0
for j in range (drawItems):
	for i in range(72):
		forward(drawLength[position])
		right(95)
	position = position+1
	forward(drawLength[position])

hideturtle()	

done()