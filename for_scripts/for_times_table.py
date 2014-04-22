#! /usr/local/bin/python3

x = int(input("Enter a number between 1 and 12: ")) #this value is going to remain fixed through the for loop below

for y in range(0,13): #for loop sets up variable y which will start at 0 and stop before 13
    print(x," x ",y," = ",x*y) #prints the result of x * y at each stage of the for loop - unlike the while loop no need to manually increment
    
        
