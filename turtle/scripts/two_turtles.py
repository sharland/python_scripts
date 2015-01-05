#! /usr/local/bin/python3

from turtle import *

andy = Turtle()     #create new object andy from class turtle
bill = Turtle()     #create new object bill from class turtle

colormode(1.0)
speed(0)

def drawCircle(t,repetition,length,turn):
    for i in range(repetition):
        t.forward(length)
        t.right(turn)

andy.pencolor("red")
drawCircle(andy,50,150,65)

bill.pencolor("blue")
drawCircle(bill,20,100,85)


done()
