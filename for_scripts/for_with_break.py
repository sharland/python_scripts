#! /usr/local/bin/python3

for x in range(1000000000):
    print(x)
    if x == 20:					#10000000000 will take a while to print so as soon as x hits 20 it will stop
        break
