#! /usr/local/bin/python3

from turtle import *
import random


title("Filling shapes")
setup(500, 500, 0, 0)
colormode(255)

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

speed(0)

iterations = random.randint(1,360)
while 360 % iterations != 0:
	iterations = random.randint(1,360)
turnValue = 360 / iterations
print(iterations)
print(turnValue)
	

begin_fill()
for j in range(iterations):
	for i in range(72):
		forward(150)
		right(95)
	right(turnValue)

end_fill()


hideturtle()
done()
