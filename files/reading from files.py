#! /usr/bin/env python3

f = open("temp","r")
print(f.readline())
print("That was the first line")
print(f.readline())
print("That was the second line")
print(f.read())
print("That was all the rest")
print(f.readline())
print("I bet that was blank")
f.close()
