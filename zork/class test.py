# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 15:04:54 2015

@author: sharland
"""

class MyClass:
    Greeting = "" #this is a class variable - not safe
    def __init__(self, Name="there"): #name definition provides default value
        self.Greeting = Name + "!"
    def SayHello(self):
        print("Hello {0}".format(self.Greeting))
        

MyInstance = MyClass() #creates an instance of MyClass named MyInstance
MyInstance.SayHello() #accesses __init__ which uses default value for name of "there"
MyInstance = MyClass("Brian") #this time provides a value which supersedes default value
MyInstance.SayHello()
