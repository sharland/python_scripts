#! /usr/bin/env python3

for x in range (1000000):
    y = x*x
    print(x,"'s square is",y)
    if y == 4096:
        break
