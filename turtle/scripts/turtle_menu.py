#! /usr/local/bin/python3

from turtle import *

speed(0)

def circle1():
	for x in range (1,73):
		forward(150)
		right(95)
		stamp()
	
	done()
	printMenu()

def circle2():
	for x in range(50,200,5):
		forward(x)
		right(90)
		stamp()

	mainloop()
	printMenu()

def printMenu():

	print('enter the number of the option you wish to run')
	print ('Run Circle 1:')
	print ('Run Circle 2:')

	menuChoice = int(input('Make your choice'))	

	if menuChoice == 1:
		circle1()
	elif menuChoice == 2:
		circle2()
	else:
		quit()
		
printMenu()

onkey(circle1,"Up")
onkey(circle2,"Down")

listen()

mainloop()
