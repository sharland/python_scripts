#! /usr/local/bin/python3

from turtle import *

setup(500,500)
colormode(255)
speed(0)


def drawShape(distance,angle,sides):
	for i in range(sides):
		forward(distance)
		right(angle)
	penup()
	forward(distance)
	pendown()
		
def fibonacci(no_shapes):
	global fib_sequence
	fib_sequence = [0,1]
	for i in range(no_shapes):
		new_fib = fib_sequence[i]+fib_sequence[i+1]
		fib_sequence.append(new_fib)
	print(fib_sequence)
	
def start():
	sides = int(input("Enter number of sides: "))
	no_shapes = int(input("Number of shapes: "))
	angle = 360/sides
	fibonacci(no_shapes)
	for i in range(no_shapes):
		distance = fib_sequence[i]
		drawShape(distance,angle,sides)
		right(i*3)
	
		
start()

done()