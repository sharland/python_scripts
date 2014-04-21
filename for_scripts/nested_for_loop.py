#! /usr/bin/env python3

for x in range(1,11):				#sets up the first for loop
    for y in range(1,11):			#nests another loop inside
        print(x,"x",y,"=",x*y)		#as y is nested inside x this will loop through 1 to 10 whilst x
									#remains at 1 - and x * y therefore create a simple times table
        
