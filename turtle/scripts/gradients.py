#! /usr/local/bin/python3

from turtle import *

setup(500,500)
tracer(0)
colormode(255)
penup()
setpos(-200,200)
pendown()
hideturtle()

print("a silly auto-gradient generator")
print("enter values from 0 to about 5 (although can go higher)")
print("can use floats")

#create lists of values for each colour
redValues = []
r = 0
changeValueR = float(input("Red change: ")) #speed of change for value
if changeValueR == 0:
    redValues.append(0)
else:
    valueRsteps = int(255/changeValueR)
    for j in range(valueRsteps):
        r += changeValueR
        redValues.append(r)

greenValues = []
g = 0
changeValueG = float(input("Green change: ")) #speed of change for value
if changeValueG == 0:
    greenValues.append(0)
else:
    valueGsteps = int(255/changeValueG)
    for j in range(valueGsteps):
        g += changeValueG
        greenValues.append(g)

blueValues = []
b = 0
changeValueB = float(input("Blue change: ")) #speed of change for value
if changeValueB == 0:
    blueValues.append(0)
else:
    valueBsteps = int(255/changeValueB)
    for j in range(valueBsteps):
        b += changeValueB
        blueValues.append(b)


redLength = len(redValues)
greenLength = len(greenValues)
blueLength = len(blueValues)

pensize(1)
pencolor(redValues[0],greenValues[0],blueValues[0])
i = -1
for j in range(400):
    right(90)
    forward(400)
    left(90)
    penup()
    forward(1)
    left(90)
    pendown()
    
    i += 1

    if i >= redLength:
        r = redValues[redLength-1]
    else:
        r = redValues[i]
    if i >= greenLength:
        g = greenValues[greenLength-1]
    else:
        g = greenValues[i]
    if i >= blueLength:
        b = blueValues[blueLength-1]
    else:
        b = blueValues[i]

    pencolor(r,g,b)
    forward(400)
    right(90)


done()
