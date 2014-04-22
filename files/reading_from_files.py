#! /usr/local/bin/python3

f = open("temp","r")
print(f.readline())								#reads the first line
print("That was the first line")
print(f.readline())								#reads the next line after the previous instruction from line 4
print("That was the second line")
print(f.read())									#reads the remainder of the file
print("That was all the rest")
print(f.readline())								#will be blank as line 8 read the rest of the file and there is nothing more
print("I bet that was blank")
f.close()
