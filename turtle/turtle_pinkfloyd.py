from turtle import *
import random

setup(600,600,0,0)
speed(0)

penup()

startX = -250
startY = 250

goto(startX,startY)
pendown()

lineXYpos = []

#print("original row")
for i in range(400):
    randTurn = random.randint(-90,90)
    right(randTurn)
    forward(2)
    setheading(0)
    currPos = []
    currPos.append(xcor())
    currPos.append(ycor())
    lineXYpos.append(currPos)
    #print(xcor(),ycor())

#print(lineXYpos)

for j in range(100):
    penup()
    startY -= 5
    goto(startX,startY)
    pendown()
    print("row {0}".format(j))
    for k in range(len(lineXYpos)):
        nextPosX = lineXYpos[k][0]
        nextPosY = lineXYpos[k][1] -(5*(j+1))
        #print(nextPosX,nextPosY)
        goto(nextPosX,nextPosY)
        

hideturtle()
done()

