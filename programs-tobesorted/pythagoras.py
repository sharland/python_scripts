#!f:
#filename: pythagoras.py
import math
def converse():
    global rightangled
    print('please enter the largest side:')
    hypothenuse = int(input())
    print('please enter the other two sides')
    side2 = int(input())
    side3 = int(input())
    rightangled = float((math.hypot(side2,side3)) == hypothenuse)
    return

converse()
if rightangled:
    print (' Right angled triangle')
else:
    print(' not right angled')
    
