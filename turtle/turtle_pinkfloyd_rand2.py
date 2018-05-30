from turtle import *
import random

setup(600,600,0,0)
speed(0)
colormode(255)

penup()

startX = -250
startY = 250

goto(startX,startY)
pendown()

lineXYpos = []

bgcolor(0,0,0)
pencolor(255,255,255)

#print("original row")
for i in range(300):
    randTurn = random.randint(-90,90)
    randDist = random.randint(0,5)
    right(randTurn)
    forward(randDist)
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
    #print("row {0}".format(j))
    for k in range(len(lineXYpos)):
        nextPosX = lineXYpos[k][0]
        randSwitch = random.randint(-1,1)
        nextPosY = lineXYpos[k][1] - (5+randSwitch)
        lineXYpos[k][1] = nextPosY #replaces previous value with new random value - should now see larger drift
        #print(nextPosX,nextPosY)
        goto(nextPosX,nextPosY)
        

hideturtle()
done()

