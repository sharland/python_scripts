#! /usr/bin/python3.3

for x in range (1000000):
    y = x*x
    print(x,"'s square is",y)
    if y == 4096:
        break
