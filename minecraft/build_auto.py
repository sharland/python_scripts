#! /usr/bin/python3


x = 0
y = 0
z = -1

for k in range(6):
	for j in range(5):
		z+=1
		for i in range(5):
			print("layer %s"%k,x,y,z)
			x+=1
		x=0
	x=0
	y+=1
	z=-1


