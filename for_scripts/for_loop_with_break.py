#! /usr/local/bin/python3

for x in range (1000000):
    y = x*x
    print(x,"'s square is",y)
    if y == 4096:					#each time the loop is run this IF is checked to see if y is equal to 4096
        break						#if it is the loop breaks
